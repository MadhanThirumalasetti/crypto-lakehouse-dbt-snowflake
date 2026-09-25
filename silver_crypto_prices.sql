{{ config(
    materialized='view',
    database='fintech_data',
    schema='silver'
) }}

SELECT
    raw_data:id::STRING AS coin_id,
    raw_data:symbol::STRING AS symbol,
    raw_data:name::STRING AS coin_name,
    raw_data:current_price::FLOAT AS current_price,
    raw_data:market_cap::FLOAT AS market_cap_usd,
    ingested_at
FROM fintech_data.bronze.raw_crypto_api
