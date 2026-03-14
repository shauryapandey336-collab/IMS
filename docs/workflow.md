# System Workflow

This document explains the workflow of the **CoreInventory – Inventory Management System** and how inventory moves through different stages inside the application.

---

## 1. User Authentication

The workflow begins when a user accesses the system.

Steps:
1. User opens the application.
2. User logs in using their credentials.
3. After successful login, the user is redirected to the **Inventory Dashboard**.

The dashboard provides an overview of the current inventory status.

---

## 2. Product Management

Before managing inventory, products must be created in the system.

Steps:
1. The user navigates to the **Products** section.
2. The user adds a new product with the following details:
   - Product Name
   - SKU / Product Code
   - Category
   - Unit of Measure
   - Initial Stock (optional)
3. The product is saved in the system and becomes available for inventory operations.

---

## 3. Receiving Goods (Receipts)

When goods arrive from a supplier, they are recorded in the system.

Steps:
1. The user opens the **Receipts** page.
2. The user creates a new receipt entry.
3. The user selects the supplier and the product.
4. The quantity of the received product is entered.
5. After validation, the stock quantity is **increased automatically**.

Example:
Receiving 50 units of a product increases the available stock by 50.

---

## 4. Delivery Orders (Outgoing Stock)

When products are shipped to customers, the delivery is recorded.

Steps:
1. The user navigates to the **Deliveries** page.
2. The user selects the product and enters the delivery quantity.
3. The delivery order is confirmed.
4. The system automatically **reduces the stock quantity**.

Example:
Delivering 10 units of a product reduces the stock by 10.

---

## 5. Internal Transfers

Products may need to be moved between warehouses or storage locations.

Steps:
1. The user opens the **Internal Transfers** section.
2. The user selects:
   - Product
   - Source location
   - Destination location
   - Quantity
3. The transfer is confirmed.

The total stock remains the same, but the **location of the stock is updated**.

---

## 6. Stock Adjustments

Sometimes the physical stock may not match the system records due to damage, loss, or counting errors.

Steps:
1. The user goes to the **Stock Adjustments** page.
2. The user selects the product and location.
3. The user enters the actual counted quantity.
4. The system updates the inventory to match the physical stock and logs the adjustment.

Example:
System shows 50 units but actual count is 47 → stock is adjusted to 47.

---

## 7. Dashboard Monitoring

The **Dashboard** provides a quick summary of inventory operations, including:

- Total products in stock
- Low stock alerts
- Pending receipts
- Pending deliveries
- Internal transfers

This helps users monitor the inventory system efficiently.

---


# System Workflow

This document explains the workflow of the **CoreInventory – Inventory Management System** and how inventory moves through different stages inside the application.

---

## 1. User Authentication

The workflow begins when a user accesses the system.

Steps:
1. User opens the application.
2. User logs in using their credentials.
3. After successful login, the user is redirected to the **Inventory Dashboard**.

The dashboard provides an overview of the current inventory status.

---

## 2. Product Management

Before managing inventory, products must be created in the system.

Steps:
1. The user navigates to the **Products** section.
2. The user adds a new product with the following details:
   - Product Name
   - SKU / Product Code
   - Category
   - Unit of Measure
   - Initial Stock (optional)
3. The product is saved in the system and becomes available for inventory operations.

---

## 3. Receiving Goods (Receipts)

When goods arrive from a supplier, they are recorded in the system.

Steps:
1. The user opens the **Receipts** page.
2. The user creates a new receipt entry.
3. The user selects the supplier and the product.
4. The quantity of the received product is entered.
5. After validation, the stock quantity is **increased automatically**.

Example:
Receiving 50 units of a product increases the available stock by 50.

---

## 4. Delivery Orders (Outgoing Stock)

When products are shipped to customers, the delivery is recorded.

Steps:
1. The user navigates to the **Deliveries** page.
2. The user selects the product and enters the delivery quantity.
3. The delivery order is confirmed.
4. The system automatically **reduces the stock quantity**.

Example:
Delivering 10 units of a product reduces the stock by 10.

---

## 5. Internal Transfers

Products may need to be moved between warehouses or storage locations.

Steps:
1. The user opens the **Internal Transfers** section.
2. The user selects:
   - Product
   - Source location
   - Destination location
   - Quantity
3. The transfer is confirmed.

The total stock remains the same, but the **location of the stock is updated**.

---

## 6. Stock Adjustments

Sometimes the physical stock may not match the system records due to damage, loss, or counting errors.

Steps:
1. The user goes to the **Stock Adjustments** page.
2. The user selects the product and location.
3. The user enters the actual counted quantity.
4. The system updates the inventory to match the physical stock and logs the adjustment.

Example:
System shows 50 units but actual count is 47 → stock is adjusted to 47.

---

## 7. Dashboard Monitoring

The **Dashboard** provides a quick summary of inventory operations, including:

- Total products in stock
- Low stock alerts
- Pending receipts
- Pending deliveries
- Internal transfers

This helps users monitor the inventory system efficiently.

---

## Overall Inventory Flow
Add Product
↓
Receive Goods (Stock In)
↓
Store in Warehouse
↓
Internal Transfers (if needed)
↓
Deliver to Customer (Stock Out)
↓
Stock Adjustment (if mismatch occurs)