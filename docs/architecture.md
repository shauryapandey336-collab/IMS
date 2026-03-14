# System Architecture

This document describes the architecture of the **CoreInventory – Inventory Management System** and how different components of the system interact with each other.

---

## Overview

The CoreInventory system is designed as a simple web-based application built using **Streamlit** for the user interface and **SQLite** for data storage. The architecture follows a lightweight structure that separates the user interface, application logic, and database layer to keep the system organized and easy to maintain.

The system allows users to manage products, record inventory transactions, and monitor stock levels through a centralized dashboard.

---

## Architecture Components

The system is divided into the following main components:

### 1. User Interface (Frontend)

The user interface is built using **Streamlit**, which allows rapid development of interactive web applications using Python.

The frontend provides pages for:
- Dashboard
- Product Management
- Receipts (Incoming Stock)
- Delivery Orders (Outgoing Stock)
- Internal Transfers
- Stock Adjustments

Users interact with the system through forms, tables, and dashboard components that display inventory data.

---

### 2. Application Logic

The application logic handles the core functionality of the system. It processes user actions and performs operations such as:

- Adding new products
- Updating stock levels
- Recording inventory transactions
- Managing stock transfers
- Adjusting inventory quantities

This logic is implemented using Python scripts that process user input from the Streamlit interface and communicate with the database.

---

### 3. Database Layer

The system uses **SQLite** as the database to store all inventory-related data. SQLite is lightweight and suitable for prototype or small-scale applications.

The database stores information such as:

- Product details
- Stock quantities
- Receipt records
- Delivery records
- Transfer records
- Stock adjustments

This ensures that inventory data is stored persistently and can be retrieved whenever needed.

---

## Data Flow

The system follows a simple data flow process:

1. The user interacts with the Streamlit interface.
2. The application processes the user's request.
3. The system reads or updates data in the SQLite database.
4. Updated results are displayed back to the user through the interface.

---

## System Architecture Diagram
User
│
▼
Streamlit Web Interface
│
▼
Application Logic (Python)
│
▼
SQLite Database

---

## Key Advantages of the Architecture

- Simple and easy to implement
- Lightweight and fast for prototypes
- Easy to maintain and extend
- Suitable for hackathon or small inventory applications

This architecture ensures that the system remains modular, scalable, and easy to understand while effectively managing inventory operations.