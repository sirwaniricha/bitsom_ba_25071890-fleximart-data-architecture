# Part 3 — Data Warehouse and Analytics

## Overview
This part focuses on building a data warehouse using dimensional modeling and performing analytical queries to support business decision-making. A star schema is designed, populated with sample data, and queried using OLAP-style SQL.

## Components
- star_schema_design.md — Documentation of the star schema, design decisions, and data flow.
- warehouse_schema.sql — SQL script to create dimension and fact tables.
- warehouse_data.sql — Sample data inserted into the data warehouse.
- analytics_queries.sql — Analytical queries for drill-down, product performance, and customer segmentation.

## Objectives
- Design a star schema optimized for analytical workloads.
- Populate the data warehouse with realistic sample data.
- Perform OLAP queries for trend analysis and segmentation.

## Workflow
1. Create dimension and fact tables in the data warehouse.
2. Load historical sales data into the warehouse.
3. Run analytical queries to derive business insights.
4. Use drill-down, aggregation, and segmentation to support reporting and decision-making.
