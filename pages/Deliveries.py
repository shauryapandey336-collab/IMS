def deliver_page():
    import streamlit as st
    import pymysql
    import pandas as pd

    st.set_page_config(page_title="Delivery Orders", layout="wide")

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="7770",
        database="odoo"
    )

    cursor = db.cursor()

    st.markdown("""
    <style>

    /* REMOVE STREAMLIT HEADER */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {display:none;}
    [data-testid="stDecoration"] {display:none;}
    [data-testid="stStatusWidget"] {display:none;}

    /* REMOVE TOP SPACE */
    .block-container{
    padding-top:0rem;
    }

    /* BACKGROUND */
    [data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    }

    /* TITLE */
    .title{
    font-size:34px;
    font-weight:800;
    color:white;
    margin-bottom:10px;
    }

    /* KPI CARDS */
    .card{
    background:rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:15px;
    box-shadow:0 10px 30px rgba(0,0,0,0.3);
    transition:0.3s;
    }

    .card:hover{
    transform:translateY(-5px);
    }

    .kpi{
    font-size:28px;
    font-weight:bold;
    color:white;
    }

    .kpi-label{
    font-size:14px;
    color:#ddd;
    }

    /* BUTTON */
    .stButton>button{
    background:linear-gradient(45deg,#ff512f,#dd2476);
    border:none;
    color:white;
    border-radius:10px;
    padding:8px 16px;
    font-weight:600;
    }

    /* TEXT COLOR */
    h1,h2,h3,label{
    color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">🚚 Delivery Orders (Outgoing Stock)</div>', unsafe_allow_html=True)

    cursor.execute("SELECT product_id, product_name, stock FROM products")
    products = cursor.fetchall()

    product_dict = {f"{p[1]} (Stock: {p[2]})": (p[0], p[2]) for p in products}

    col1,col2,col3 = st.columns(3)

    total_products = len(products)
    total_stock = sum(p[2] for p in products)

    cursor.execute("SELECT COUNT(*) FROM deliveries")
    deliveries = cursor.fetchone()[0]

    with col1:
        st.markdown(f"""
        <div class="card">
        <div class="kpi">{total_products}</div>
        <div class="kpi-label">Products</div>
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
        <div class="kpi">{total_stock}</div>
        <div class="kpi-label">Total Stock</div>
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
        <div class="kpi">{deliveries}</div>
        <div class="kpi-label">Deliveries</div>
        </div>
        """,unsafe_allow_html=True)

    st.divider()

    with st.form("delivery_form"):

        col1,col2 = st.columns(2)

        with col1:
            customer_name = st.text_input("👤 Customer Name")
            product_name = st.selectbox("📦 Select Product", list(product_dict.keys()))

        with col2:
            quantity = st.number_input("🔢 Quantity", min_value=1)
            location = st.text_input("📍 Delivery Location")

        submit = st.form_submit_button("✅ Confirm Delivery")

    if submit:

        if customer_name and product_name and location:

            product_id, current_stock = product_dict[product_name]

            if quantity > current_stock:
                st.error("❌ Not enough stock available!")

            else:

                cursor.execute("""
                    INSERT INTO deliveries (customer_name, product_id, quantity, location, status)
                    VALUES (%s,%s,%s,%s,'Completed')
                """,(customer_name,product_id,quantity,location))

                cursor.execute("""
                    UPDATE products
                    SET stock = stock - %s
                    WHERE product_id=%s
                """,(quantity,product_id))

                db.commit()

                st.success("✅ Delivery successful! Stock updated.")

        else:
            st.warning("⚠️ Fill all fields")

    st.subheader("📊 Recent Deliveries")

    cursor.execute("""
        SELECT d.delivery_id, d.customer_name, p.product_name,
            d.quantity, d.location, d.status, d.created_at
        FROM deliveries d
        JOIN products p ON d.product_id = p.product_id
        ORDER BY d.delivery_id DESC
    """)

    data = cursor.fetchall()

    df = pd.DataFrame(data,columns=[
        "ID","Customer","Product","Quantity","Location","Status","Date"
    ])

    st.dataframe(df,use_container_width=True)

    st.divider()

    st.subheader("⚠️ Low Stock Alerts")

    low_stock = [p for p in products if p[2] < 20]

    if low_stock:

        alert_df = pd.DataFrame(low_stock,columns=["ID","Product","Stock"])

        st.warning("Some products are running low!")

        st.dataframe(alert_df,use_container_width=True)

    else:

        st.success("All products have sufficient stock!")