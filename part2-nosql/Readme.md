# Part 2 — NoSQL Database Analysis

## Overview
This part evaluates the suitability of MongoDB for handling highly diverse and evolving product data. It includes both a theoretical justification for using a NoSQL database and practical MongoDB operations on a sample product catalog.

## Components
- nosql_analysis.md — Theoretical analysis of RDBMS limitations, MongoDB benefits, and trade-offs.
- mongodb_operations.js — MongoDB commands for loading data, querying, updating, and aggregating.
- products_catalog.json — Sample product catalog with nested specifications and reviews.

## Objectives
- Analyze why relational databases are not ideal for highly heterogeneous product data.
- Demonstrate how MongoDB’s document-based model supports flexibility and scalability.
- Perform real MongoDB operations such as filtering, aggregation, and document updates.

## Workflow
1. Product catalog data is stored as JSON documents.
2. Data is loaded into MongoDB.
3. Queries are executed for filtering, review analysis, and category-level aggregation.
4. Results demonstrate MongoDB’s capability to handle nested and semi-structured data efficiently.
