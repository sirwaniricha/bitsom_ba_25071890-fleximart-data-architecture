# Star Schema Design

## Section 1: Schema Overview

FACT TABLE: fact_sales  
Grain: One row per product per order line item  
Business Process: Sales transactions  

Measures:
- quantity_sold
- unit_price
- discount_amount
- total_amount  

Foreign Keys:
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer  

DIMENSION: dim_date  
Purpose: Time-based analysis  
Attributes: date_key, full_date, day_of_week, month, month_name, quarter, year, is_weekend  

DIMENSION: dim_product  
Purpose: Product analysis  
Attributes: product_key, product_id, product_name, category, subcategory, unit_price  

DIMENSION: dim_customer  
Purpose: Customer analysis  
Attributes: customer_key, customer_id, customer_name, city, state, customer_segment  

---

## Section 2: Design Decisions (150 words)

The chosen granularity is transaction line-item level because it captures the most detailed level of sales activity, allowing flexible aggregation across time, product, and customer dimensions. This enables drill-down from monthly to daily or even per-product sales.

Surrogate keys are used instead of natural keys because they are stable, compact, and independent of business logic. Natural keys such as product IDs or customer IDs may change or have formatting inconsistencies.

This design supports drill-down and roll-up operations by organizing facts around conformed dimensions. Analysts can aggregate sales by year, quarter, or month, and further drill down into product categories or customer segments.

---

## Section 3: Sample Data Flow

Source:
Order #101, Customer "John Doe", Product "Laptop", Qty: 2, Price: 50000

fact_sales:
(date_key=20240115, product_key=5, customer_key=12, quantity_sold=2, unit_price=50000, total_amount=100000)

dim_date:
(date_key=20240115, full_date='2024-01-15', month=1, quarter='Q1')

dim_product:
(product_key=5, product_name='Laptop', category='Electronics')

dim_customer:
(customer_key=12, customer_name='John Doe', city='Mumbai')
