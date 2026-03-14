def transfer_page():
    import streamlit as st
    import pymysql as sql
    import pandas as pd

    st.set_page_config(page_title="Internal Transfers", layout="wide")

    db = sql.connect(
        host="localhost",
        user="root",
        password="7770",
        database="odoo"
    )

    cursor = db.cursor()

    st.markdown("""
    <style>

    /* REMOVE STREAMLIT HEADER */
    header {visibility:hidden;}
    footer {visibility:hidden;}
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
    font-size:32px;
    font-weight:bold;
    color:white;
    margin-bottom:10px;
    }

    /* FORM CARD */
    [data-testid="stForm"]{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
    padding:25px;
    border-radius:15px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.3);
    }

    /* BUTTON */
    .stButton>button{
    background:linear-gradient(45deg,#ff512f,#dd2476);
    color:white;
    border:none;
    border-radius:8px;
    padding:10px 20px;
    font-size:16px;
    }

    h1,h2,h3,label{
    color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">🔄 Internal Transfers</div>', unsafe_allow_html=True)

    cursor.execute("SELECT product_id, product_name, stock, location FROM products")
    products = cursor.fetchall()

    product_dict = {
        f"{p[1]} (Stock: {p[2]} | Location: {p[3]})": (p[0], p[2], p[3])
        for p in products
    }

    with st.form("transfer_form"):

        col1, col2 = st.columns(2)

        with col1:
            product_name = st.selectbox("📦 Select Product", list(product_dict.keys()))
            from_location = st.text_input("📍 From Location")

        with col2:
            to_location = st.text_input("📍 To Location")
            quantity = st.number_input("🔢 Quantity", min_value=1)

        submit = st.form_submit_button("🔁 Transfer")

    if submit:

        if product_name and from_location and to_location and quantity:

            product_id, current_stock, current_location = product_dict[product_name]

            if quantity > current_stock:
                st.error("❌ Not enough stock available!")

            elif from_location == to_location:
                st.warning("⚠️ From and To location cannot be same!")

            else:

                cursor.execute("""
                    INSERT INTO transfers (product_id, from_location, to_location, quantity, status)
                    VALUES (%s,%s,%s,%s,'Completed')
                """,(product_id,from_location,to_location,quantity))

                cursor.execute("""
                    UPDATE products
                    SET location=%s
                    WHERE product_id=%s
                """,(to_location,product_id))

                db.commit()

                st.success("✅ Transfer successful!")

    st.markdown("### 📊 Transfer History")

    cursor.execute("""
    SELECT t.transfer_id,p.product_name,t.from_location,t.to_location,
    t.quantity,t.status,t.created_at
    FROM transfers t
    JOIN products p ON t.product_id=p.product_id
    ORDER BY t.transfer_id DESC
    """)

    data = cursor.fetchall()

    df = pd.DataFrame(data,columns=[
    "ID","Product","From Location","To Location","Quantity","Status","Date"
    ])

    st.dataframe(df,use_container_width=True)