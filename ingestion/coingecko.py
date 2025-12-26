import requests
import logging
from core.db import SessionLocal
from core.models import RawCryptoData

logging.basicConfig(level=logging.INFO)

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False
}

def fetch_and_store_coingecko():
    db = SessionLocal()

    # 🔁 INCREMENTAL CHECK
    existing = db.query(RawCryptoData).filter_by(source="coingecko").first()
    if existing:
        logging.info("CoinGecko data already ingested. Skipping.")
        db.close()
        return

    response = requests.get(COINGECKO_URL, params=PARAMS, timeout=10)
    response.raise_for_status()

    data = response.json()
    logging.info(f"Fetched {len(data)} records from CoinGecko")

    try:
        record = RawCryptoData(
            source="coingecko",
            data=data
        )
        db.add(record)
        db.commit()
        logging.info("CoinGecko data stored successfully")
    except Exception as e:
        db.rollback()
        logging.error(f"DB error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    fetch_and_store_coingecko()
