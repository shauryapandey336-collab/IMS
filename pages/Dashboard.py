import streamlit as st
def kpi_card(title, value, color):
    st.markdown(f"""
    <style>

    .kpi-wrapper {{
        padding:10px;
    }}

    .kpi-card {{
        width:170px;
        height:170px;
        border-radius:18px;
        background:{color};
        color:white;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        text-align:center;
        font-family:'Segoe UI', sans-serif;
        box-shadow:0 8px 25px rgba(0,0,0,0.15);
        transition: all 0.35s ease;
        position:relative;
        overflow:hidden;
    }}

    /* glass shine effect */
    .kpi-card:before {{
        content:'';
        position:absolute;
        top:0;
        left:-75%;
        width:50%;
        height:100%;
        background:rgba(255,255,255,0.3);
        transform:skewX(-25deg);
        transition:0.5s;
    }}

    .kpi-card:hover:before {{
        left:120%;
    }}

    .kpi-card:hover {{
        transform:translateY(-8px) scale(1.05);
        box-shadow:0 20px 40px rgba(0,0,0,0.3);
        cursor:pointer;
    }}

    .kpi-title {{
        font-size:16px;
        font-weight:600;
        margin-bottom:8px;
    }}

    .kpi-value {{
        font-size:36px;
        font-weight:700;
    }}

    </style>

    <div class="kpi-wrapper">
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# DASHBOARD FUNCTION



    st.title("📦 Inventory Dashboard")
    total_products = 250
    low_stock = 19
    pending_receipts = 18
    pending_deliveries = 12
    internal_transfers = 8
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")
    with col1:
        kpi_card("Total Products", total_products,
                 "linear-gradient(135deg,#00c6ff,#0072ff)")
    with col2:
        kpi_card("Low Stock Items", low_stock,
                 "linear-gradient(135deg,#ff9966,#ff5e62)")
    with col3:
        kpi_card("Pending Receipts", pending_receipts,
                 "linear-gradient(135deg,#56ab2f,#a8e063)")
    with col4:
        kpi_card("Pending Deliveries", pending_deliveries,
                 "linear-gradient(135deg,#ff512f,#dd2476)")
    with col5:
        kpi_card("Internal Transfers", internal_transfers,
                 "linear-gradient(135deg,#7f00ff,#e100ff)")
    st.subheader("Filter Summary")
    st.subheader("Inventory Data")
    data = {
        "Product": ["Item A", "Item B", "Item C"],
        "Stock": [50, 10, 5],
        "Warehouse": ["Warehouse A", "Warehouse B", "Warehouse A"],
        "Category": ["Electronics", "Clothing", "Food"]
    }
    st.table(data)
show_dashboard()