import streamlit as st
import pandas as pd 
import pymysql as sql

# ---------- DATABASE CONNECTION ----------
db = sql.connect(
    host="localhost",
    user="root",
    password="7770",
    database="odoo"
)

cursor = db.cursor()

# ---------- INLINE CSS ----------


def product_page():
    st.markdown("""
<style>

/* Force all text black */
html, body, p, span, div, label, h1, h2, h3, h4, h5, h6{
color:black !important;
}

/* Tabs text */
button[role="tab"]{
color:black !important;
}

/* Input labels */
label{
color:black !important;
}

/* Text input */
.stTextInput input{
color:black !important;
border-radius:8px;
padding:10px;
border:1px solid #ccc;
box-shadow:0 3px 10px rgba(0,0,0,0.1);
}

/* Number input */
.stNumberInput input{
color:black !important;
border-radius:8px;
padding:10px;
border:1px solid #ccc;
box-shadow:0 3px 10px rgba(0,0,0,0.1);
}

/* Selectbox */
.stSelectbox div{
border-radius:8px;
box-shadow:0 3px 10px rgba(0,0,0,0.1);
}

/* Selectbox selected text black */
div[data-baseweb="select"] *{
color:black !important;
}

/* Dropdown options white */
div[role="listbox"] *{
color:black !important;
}

/* Checkbox text white */
.stCheckbox label{
color:black !important;
}

/* Light background */
[data-testid="stAppViewContainer"]{
background:linear-gradient(135deg,#e3f2fd,#bbdefb);
}

/* Dark mode background */
@media (prefers-color-scheme: dark){
[data-testid="stAppViewContainer"]{
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}
}

/* Tabs card */
.stTabs{
background:white;
padding:25px;
border-radius:15px;
box-shadow:0 15px 40px rgba(0,0,0,0.25);
transition:0.3s;
}

/* Hover card */
.stTabs:hover{
transform:translateY(-5px);
box-shadow:0 20px 50px rgba(0,0,0,0.35);
}

/* Buttons */
.stButton>button{
width:100%;
background:linear-gradient(45deg,#ff6a00,#ee0979);
color:white;
border:none;
border-radius:10px;
padding:12px;
font-size:16px;
transition:0.3s;
box-shadow:0 8px 20px rgba(0,0,0,0.25);
}

/* Button hover */
.stButton>button:hover{
transform:scale(1.05);
box-shadow:0 12px 30px rgba(0,0,0,0.35);
background:linear-gradient(45deg,#ff512f,#dd2476);
}

/* Dataframe */
[data-testid="stDataFrame"]{
border-radius:12px;
box-shadow:0 10px 30px rgba(0,0,0,0.25);
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:#1f2937;
color:white;
}

</style>
""", unsafe_allow_html=True)


    add, edit, delete = st.tabs(["Add Product", "Edit Product", "Delete Product"])

    with add:

        st.title("📦 Product Management")
        st.subheader("Create New Product")

        a = st.text_input("Enter Product Name")
        b = st.text_input("Enter SKU Code")

        c = st.selectbox(
            "Select Category",
            ["Raw Materials", "Finished Goods", "Work-in-Progress (WIP)", "Consumables", "Spare Parts"]
        )

        d = st.selectbox(
            "Unit of Measure",
            ["Piece", "Kg", "Gram", "Liter", "Meter"]
        )

        e = st.number_input("Enter Initial Stock", min_value=0, step=1)

        f = st.selectbox(
            "Location",
            ["Gwalior", "Indore", "Bhopal", "Pune", "Mumbai", "Bangalore"]
        )

        if st.button("Add Product"):

            try:

                q = """
                INSERT INTO products 
                (product_name, sku, category, unit, stock, location) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """

                cursor.execute(q, (a,b,c,d,e,f))
                db.commit()

                st.success("Product Added Successfully!")

            except Exception as err:

                st.error(f"Error: {err}")

    with edit:

        st.subheader("Edit Product")

        product_id = st.number_input("Enter Product ID", min_value=1)
        new_stock = st.number_input("Update Stock", min_value=0)
        loc = st.text_input("Enter the New Location ")

        if st.button("Update Product"):

            try:

                q = "UPDATE products SET stock=%s,location=%s WHERE product_id=%s"

                cursor.execute(q,(new_stock,loc,product_id))
                db.commit()

                st.success("Product Updated Successfully!")

            except Exception as err:

                st.error(f"Error: {err}")

    with delete:

        st.subheader("🗑️ Delete Product")

        d_id = st.number_input("Enter Product ID to Delete", min_value=1)

        if st.button("Delete Product"):

            try:

                q = "DELETE FROM products WHERE product_id=%s"

                cursor.execute(q,(d_id,))
                db.commit()

                st.success("Product Deleted Successfully!")

            except Exception as err:

                st.error(f"Error: {err}")