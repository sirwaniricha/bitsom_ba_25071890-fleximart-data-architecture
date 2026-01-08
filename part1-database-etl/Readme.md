# Part 1 — Database Design and ETL Pipeline

## Overview
This part focuses on building an end-to-end ETL pipeline to clean raw CSV data and load it into a relational database. It also includes database schema documentation and SQL queries to answer business questions.

## Components
- etl_pipeline.py — Extracts, cleans, transforms, and loads data into MySQL.
- schema_documentation.md — Documents schema, normalization, and relationships.
- business_queries.sql — Business analytics queries.
- data_quality_report.txt — ETL summary report.
- requirements.txt — Python dependencies.

## Workflow
1. Raw CSV files are read using pandas.
2. Data quality issues such as duplicates, missing values, and inconsistent formats are handled.
3. Cleaned data is inserted into the database.
4. Business queries are executed on the clean data.
