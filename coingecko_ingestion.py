import requests
import json
import snowflake.connector

# 1. Fetch live market data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
response = requests.get(url)
data = response.json()

# 2. Connect to Snowflake (Update with your credentials)
conn = snowflake.connector.connect(
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='DBT_DEV_WH',
    database='FINTECH_DATA',
    schema='BRONZE'
)
cursor = conn.cursor()

# 3. Load raw JSON payload into Bronze layer
for coin in data:
    raw_json = json.dumps(coin).replace("'", "''")
    query = f"""
        INSERT INTO raw_crypto_api (raw_data, ingested_at)
        SELECT PARSE_JSON('{raw_json}'), CURRENT_TIMESTAMP();
    """
    cursor.execute(query)

print("Successfully ingested live CoinGecko data into Snowflake Bronze layer.")
