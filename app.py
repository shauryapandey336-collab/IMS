import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from reglog import login_page
from Dashboard import show_dashboard
from Product_Man import product_page 
from receipt import receipt_page
from deliveries import deliver_page
from transfers import transfer_page
from adjustment import adjustment_page

st.set_page_config(page_title="CoreInventory", layout="wide")

# -------- SESSION INIT --------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# -------- ROUTING --------
if not st.session_state.logged_in:
    login_page()

else:
    # -------- SIDEBAR --------
    st.sidebar.title("📦 Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Dashboard", "Product Management","receipt","Deliveries","Transfer","adjustment"]
    )

    # -------- LOGOUT --------
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "Login"
        st.rerun()

    # -------- PAGE SWITCH --------
    if page == "Dashboard":
        show_dashboard()

    elif page == "Product Management":
        product_page()
    elif page =="receipt":
        receipt_page()
    elif page=="Deliveries":
        deliver_page()
    elif page=="Transfer":
        transfer_page()
    elif page=="adjustment":
        adjustment_page()