# Real-Time Crypto Medallion Pipeline (Snowflake + dbt)

An end-to-end FinTech ELT pipeline implementing a modern Databricks-style Medallion Architecture (Bronze → Silver → Gold) using Python, Snowflake, and dbt Cloud.

---

## Architecture Overview

1. **Extraction & Ingestion (Python / Colab):** Fetches live market data from CoinGecko REST API and appends raw JSON payloads into Snowflake.
2. **Bronze Layer (`raw_crypto_api`):** Unparsed raw JSON data stored with ingestion timestamps for auditability and replayability.
3. **Silver Layer (`silver_crypto_prices`):** dbt view parsing semi-structured JSON elements into flattened, typed relational attributes.
4. **Gold Layer (`gold_crypto_metrics`):** Incremental analytics model calculating market rankings, valuations, and tracking price volatility.

---

## Tech Stack

- **Data Warehouse:** Snowflake (Multi-cluster virtual warehouse, RBAC management)
- **Transformation:** dbt Cloud (Version control, testing, view/table materializations)
- **Ingestion:** Python (`requests`, `snowflake-connector-python`)
- **Data Source:** CoinGecko REST API v3

---

## Medallion Architecture Design

| Layer | Object Name | Materialization | Purpose |
| :--- | :--- | :--- | :--- |
| **Bronze** | `raw_crypto_api` | Table | Immutable raw JSON storage with audit timestamps |
| **Silver** | `silver_crypto_prices` | View | Flattens semi-structured JSON into relational schema |
| **Gold** | `gold_crypto_metrics` | Table / Incremental | Aggregated metrics, rankings, and business-ready stats |

---

## Role-Based Access Control (RBAC) & Engineering Highlights

- Configured custom schemas (`DBT_MTHIRUMALASETTI_SILVER`, `DBT_MTHIRUMALASETTI_GOLD`) with strict principle-of-least-privilege permissions.
- Resolved cross-database compilation access controls between ingestion and transformation service roles (`PC_DBT_ROLE`).
- Automated schema migrations directly integrated with GitHub version control and dbt Cloud CI runs.
