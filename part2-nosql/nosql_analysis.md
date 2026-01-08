# NoSQL Analysis for FlexiMart Product Catalog

## Section A: Limitations of RDBMS (150 words)

Relational databases such as MySQL use fixed schemas, which makes them unsuitable for handling highly diverse product types. In FlexiMart’s catalog, different products require different attributes — laptops need RAM and processor details, while shoes require size and color. Representing this in a relational schema would require many nullable columns or multiple subtype tables, making the design complex and inefficient.

Frequent schema changes are another issue. Each time a new product type is introduced, the database schema must be altered, which is costly, risky in production environments, and causes downtime.

Storing nested data such as customer reviews is also inefficient in RDBMS. Reviews must be stored in separate tables and joined during queries, increasing query complexity and reducing read performance. This makes the system harder to maintain and slower for analytical or read-heavy workloads.

---

## Section B: NoSQL Benefits (150 words)

MongoDB uses a flexible document-based schema that allows each product to store only the fields it needs. A laptop document can contain specifications like RAM and CPU, while a shoe document can store size and color without any schema changes. This flexibility supports rapid evolution of the product catalog.

MongoDB also supports embedded documents, allowing reviews to be stored directly inside product documents. This improves read performance and simplifies data retrieval by avoiding joins.

Additionally, MongoDB is designed for horizontal scalability using sharding. As FlexiMart’s catalog and traffic grow, MongoDB can distribute data across multiple servers, ensuring high availability and performance. This makes MongoDB well-suited for handling large-scale, dynamic, and semi-structured data such as diverse product catalogs.

---

## Section C: Trade-offs (100 words)

MongoDB provides weaker transactional guarantees compared to relational databases, especially for multi-document transactions, which can be problematic for financial consistency. It also lacks strict schema enforcement, increasing the risk of inconsistent or malformed data if proper validation is not implemented. Moreover, complex analytical queries are often easier to write and optimize in SQL than in MongoDB’s aggregation framework.
