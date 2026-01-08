import pandas as pd
import mysql.connector
from datetime import datetime
import re

# ---------- CONFIG ----------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "fleximart"
}

REPORT = []

# ---------- UTILS ----------
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r'\D', '', str(phone))
    if digits.startswith('91'):
        digits = digits[2:]
    if len(digits) == 10:
        return "+91-" + digits
    return None

def standardize_date(date_str):
    try:
        return pd.to_datetime(date_str, dayfirst=True).date()
    except:
        return None

# ---------- EXTRACT ----------
customers = pd.read_csv("../data/customers_raw.csv")
products = pd.read_csv("../data/products_raw.csv")
sales = pd.read_csv("../data/sales_raw.csv")

REPORT.append(f"Customers raw: {len(customers)}")
REPORT.append(f"Products raw: {len(products)}")
REPORT.append(f"Sales raw: {len(sales)}")

# ---------- TRANSFORM ----------
# Deduplicate
customers_before = len(customers)
customers = customers.drop_duplicates()
REPORT.append(f"Customer duplicates removed: {customers_before - len(customers)}")

# Handle missing emails → drop
missing_email = customers['email'].isna().sum()
customers = customers.dropna(subset=['email'])
REPORT.append(f"Customers dropped due to missing email: {missing_email}")

customers['phone'] = customers['phone'].apply(standardize_phone)
customers['registration_date'] = customers['registration_date'].apply(standardize_date)

# Products
missing_price = products['price'].isna().sum()
products['price'] = products['price'].fillna(products['price'].median())
products['stock_quantity'] = products['stock_quantity'].fillna(0)
products['category'] = products['category'].str.strip().str.lower().str.title()
REPORT.append(f"Products missing price filled: {missing_price}")

# ---------- LOAD ----------
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

for _, r in customers.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO customers (first_name,last_name,email,phone,city,registration_date)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(r[1:]))

for _, r in products.iterrows():
    cursor.execute("""
        INSERT INTO products (product_name,category,price,stock_quantity)
        VALUES (%s,%s,%s,%s)
    """, (r['product_name'], r['category'], r['price'], int(r['stock_quantity'])))

conn.commit()
conn.close()

REPORT.append("Load completed successfully.")

with open("data_quality_report.txt", "w") as f:
    f.write("\n".join(REPORT))
