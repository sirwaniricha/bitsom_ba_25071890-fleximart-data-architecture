# bitsom_ba_25071890-fleximart-data-architecture
 
# FlexiMart Data Architecture Project

**Student Name:** Richa Sirwani
**Student ID:** bitsom_ba_25071890
**Email:** sirwani.richa@gmail.com
**Date:** 08/01/2026

## Project Overview

Submission for Module 2

## Repository Structure
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md

## Technologies Used

- Python 3.x, pandas, mysql-connector-python
- MySQL 8.0 / PostgreSQL 14
- MongoDB 6.0

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql


### MongoDB Setup

mongosh < part2-nosql/mongodb_operations.js

## Key Learnings

This project helped me understand how data moves across different systems — from raw operational data to a structured data warehouse and analytical layer. I learned how to design and implement ETL pipelines, handle real-world data quality issues, and model data using both relational and NoSQL approaches. I also gained practical experience in dimensional modeling using star schemas and writing analytical SQL queries for business reporting. Overall, the project strengthened my understanding of how backend data engineering supports business decision-making.

## Challenges Faced

Handling inconsistent and incomplete raw data
The raw CSV files contained missing values, duplicates, and inconsistent formats. I addressed this by implementing data cleaning rules in the ETL pipeline such as deduplication, standardization, and default value handling before loading data into the database.

Designing schemas that balance flexibility and structure
Choosing between relational and NoSQL models was challenging because both have different strengths. I resolved this by using a relational model for transactional and analytical consistency, and MongoDB for flexible, evolving product data, ensuring the architecture supports both operational reliability and future scalability.


