Entity: customers

Purpose: Stores registered customer information.

Attributes:

customer_id (PK): Unique surrogate identifier

first_name: Customer first name

last_name: Customer last name

email: Unique contact email

phone: Standardized phone number

city: City of residence

registration_date: Date of registration

Relationships:

One customer places many orders (1:M → orders).

Normalization (3NF — 200+ words)

The schema is in Third Normal Form (3NF) because each table stores facts about a single entity and all non-key attributes depend only on the primary key. In the customers table, attributes such as first_name, last_name, email, phone, city, and registration_date depend solely on customer_id. There are no transitive dependencies — for example, city does not determine state or region.

In products, price and stock_quantity depend only on product_id. Category is descriptive and does not determine any other attribute. In orders, total_amount and status depend only on order_id, and customer_id acts purely as a foreign key.

This design avoids update anomalies by isolating each entity. A customer’s phone number update affects only one row. Insert anomalies are avoided because new products or customers can be added independently without requiring order data. Delete anomalies are avoided because deleting an order does not remove customer or product data.

Functional dependencies:

customer_id → first_name, last_name, email, phone, city, registration_date

product_id → product_name, category, price, stock_quantity

order_id → customer_id, order_date, total_amount, status