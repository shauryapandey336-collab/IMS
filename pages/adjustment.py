def adjustment_page():
    import streamlit as st
    import pymysql

    st.set_page_config(page_title="Stock Adjustment", layout="wide")

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="7770",
        database="odoo"
    )

    cursor = db.cursor()

    # ---------------- ADVANCED CSS ----------------

    st.markdown("""
    <style>

    /* Hide streamlit header space */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Remove top white block */
    .block-container{
    padding-top: 1rem;
    }

    /* Background */
    .stApp{
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color:white;
    }

    /* Labels visible */
    label{
    color:white !important;
    font-weight:600;
    }

    /* Input fields */
    input{
    background:white !important;
    color:black !important;
    border-radius:8px !important;
    }

    /* Selectbox */
    div[data-baseweb="select"]{
    background:white !important;
    border-radius:8px;
    color:black;
    }

    /* Number input */
    div[data-baseweb="input"]{
    background:white !important;
    border-radius:8px;
    }

    /* Buttons */
    .stButton>button{
    background:#ff7f50;
    color:white;
    border-radius:10px;
    padding:10px 25px;
    font-weight:bold;
    border:none;
    }

    .stButton>button:hover{
    background:#ff5722;
    }

    /* Table */
    [data-testid="stDataFrame"]{
    background:white;
    color:black;
    border-radius:10px;
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------------- TITLE ----------------

    st.markdown('<div class="main-title">⚖️ Smart Stock Adjustment</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Fix inventory mismatch between system stock and actual warehouse stock</div>', unsafe_allow_html=True)


    # ---------------- FETCH PRODUCTS ----------------

    cursor.execute("SELECT product_id, product_name, stock, location FROM products")
    products = cursor.fetchall()

    product_dict = {
        f"{p[1]}  |  Stock:{p[2]}  |  {p[3]}": (p[0], p[2], p[3])
        for p in products
    }


    # ---------------- FORM ----------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    with st.form("adjust_form"):

        col1,col2 = st.columns(2)

        with col1:
            selected_product = st.selectbox("📦 Select Product", list(product_dict.keys()))
            location = st.text_input("📍 Location")

        with col2:
            system_qty = st.number_input("📊 System Quantity", min_value=0, step=1)
            actual_qty = st.number_input("📦 Actual Quantity", min_value=0, step=1)

        st.write("")

        submit = st.form_submit_button("⚖️ Adjust Stock")

    st.markdown('</div>', unsafe_allow_html=True)


    # ---------------- LOGIC ----------------

    if submit:

        if selected_product and location:

            product_id,current_stock,current_location = product_dict[selected_product]

            difference = actual_qty - system_qty

            cursor.execute("""
            INSERT INTO adjustments (product_id, location, system_quantity, actual_quantity, difference)
            VALUES (%s,%s,%s,%s,%s)
            """,(product_id,location,system_qty,actual_qty,difference))


            cursor.execute("""
            UPDATE products
            SET stock=%s
            WHERE product_id=%s
            """,(actual_qty,product_id))


            db.commit()

            if difference>0:
                st.success(f"✅ Stock Increased by {difference}")

            elif difference<0:
                st.warning(f"⚠️ Stock Decreased by {abs(difference)}")

            else:
                st.info("ℹ️ No Stock Change")

        else:
            st.error("❌ Please fill all fields")


    # ---------------- HISTORY ----------------

    st.markdown("## 📊 Adjustment History")

    cursor.execute("""
    SELECT a.adjustment_id,
    p.product_name,
    a.location,
    a.system_quantity,
    a.actual_quantity,
    a.difference,
    a.created_at
    FROM adjustments a
    JOIN products p ON a.product_id=p.product_id
    ORDER BY a.adjustment_id DESC
    """)

    rows = cursor.fetchall()

    st.dataframe(rows,use_container_width=True)