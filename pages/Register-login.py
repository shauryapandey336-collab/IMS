import streamlit as st
import pymysql as sql

def login_page():
    db = sql.connect(
        host="localhost",
        user="root",
        password="Yoge@2006",
        database="odoo"
    )
    smt = db.cursor()

    if "verified" not in st.session_state:
        st.session_state.verified = False

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user_email" not in st.session_state:
        st.session_state.user_email = ""

    # -------- CSS --------
    st.markdown("""
<style>

/* -------- FORCE PAGE RESET -------- */
html, body, [class*="css"]  {
    margin:0 !important;
    padding:0 !important;
}

/* -------- REMOVE DEFAULT WIDTH -------- */
.block-container {
    max-width: 100% !important;
    padding: 0 !important;
}

/* -------- FULL SCREEN CENTER -------- */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg,#e0ecff,#f5f7fa,#dbeafe);
}

/* -------- MAIN CENTER FIX -------- */
section.main > div {
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}

/* -------- FIX EXTRA WRAPPERS -------- */
div[data-testid="stVerticalBlock"] {
    width:100%;
    display:flex;
    justify-content:center;
}

/* -------- CARD -------- */
.main-card {
    width:420px !important;
    padding:30px;

    border-radius:20px;
    background:white;

    box-shadow:0 20px 60px rgba(0,0,0,0.2);

    color:black;
}

/* -------- INPUT FIX -------- */
.stTextInput, .stSelectbox {
    width:100% !important;
}

/* -------- BUTTON -------- */
.stButton>button {
    width:100%;
    background:white;
    color:white;
    border:none;
    border-radius:10px;
    padding:12px;
    font-size:16px;
}

/* -------- RADIO CENTER -------- */
div[role="radiogroup"]{
    justify-content:center;
}

/* -------- HIDE SIDEBAR WHEN LOGIN -------- */
section[data-testid="stSidebar"] {
    display:none !important;
}

</style>
""", unsafe_allow_html=True)
    if st.session_state.logged_in:

        st.success(f"Welcome {st.session_state.user_email} 🎉")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.rerun()

    else:

        st.markdown('<div class="main-card"><h2 style="text-align:center;">CoreInventory System</h2>', unsafe_allow_html=True)

        page = st.radio("", ["Login","Sign Up","Forgot Password"], horizontal=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        if page == "Login":

            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                smt.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
                user = smt.fetchone()

                if user:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.rerun()
                else:
                    st.error("Invalid Email or Password")

        elif page == "Sign Up":

            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            password = st.text_input("Password", type="password")

            role = st.selectbox("Role", ["Inventory Manager","Warehouse Staff"])

            if st.button("Create Account"):
                try:
                    smt.execute(
                        "INSERT INTO users (full_name, email, phone_number, password, role) VALUES (%s,%s,%s,%s,%s)",
                        (name, email, phone, password, role)
                    )
                    db.commit()
                    st.success("Account Created")
                except:
                    st.error("Email or Phone already exists")

        elif page == "Forgot Password":

            if not st.session_state.verified:

                email = st.text_input("Registered Email")

                if st.button("Verify Email"):
                    smt.execute("SELECT * FROM users WHERE email=%s", (email,))
                    user = smt.fetchone()

                    if user:
                        st.session_state.verified = True
                        st.session_state.reset_email = email
                        st.rerun()
                    else:
                        st.error("Email not registered")

            else:

                new_password = st.text_input("New Password", type="password")
                confirm_password = st.text_input("Rewrite Password", type="password")

                if st.button("Update Password"):

                    if new_password != confirm_password:
                        st.error("Passwords do not match")
                    else:
                        smt.execute(
                            "UPDATE users SET password=%s WHERE email=%s",
                            (new_password, st.session_state.reset_email)
                        )
                        db.commit()
                        st.session_state.verified = False
                        st.success("Password Updated")
                        st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)