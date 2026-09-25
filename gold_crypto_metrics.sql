{{ config(
    materialized='table',
    database='fintech_data',
    schema='gold'
) }}

SELECT
    coin_id,
    symbol,
    coin_name,
    current_price,
    market_cap_usd,
    ingested_at AS last_updated_at
FROM {{ ref('silver_crypto_prices') }}
ORDER BY market_cap_usd DESC
