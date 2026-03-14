# CoreInventory – Inventory Management System

## Overview

CoreInventory is a simple **inventory management dashboard** built using **Python and Streamlit**.
It helps users manage products and track inventory operations like **receipts, deliveries, transfers, and stock adjustments** from a single interface.

---

## Features

* Login Authentication
* Inventory Dashboard with KPI cards
* Product Management
* Stock Receipts
* Deliveries Tracking
* Warehouse Transfers
* Stock Adjustments
* Sidebar Navigation

---

## Tech Stack

* Python
* Streamlit
* ReportLab

---

## Project Structure

```
app.py              # Main application
reglog.py           # Login system
Dashboard.py        # Inventory dashboard
Product_Man.py      # Product management
receipt.py          # Receipts module
deliveries.py       # Deliveries module
transfers.py        # Transfers module
adjustment.py       # Stock adjustment module
```

---

## How to Run

Install dependencies:

```
pip install streamlit reportlab pandas plotly
```

Run the application:

```
streamlit run app.py
```

---
