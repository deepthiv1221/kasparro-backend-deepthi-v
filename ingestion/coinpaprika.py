import requests
import logging
from core.db import SessionLocal
from core.models import RawCryptoData

logging.basicConfig(level=logging.INFO)

COINPAPRIKA_URL = "https://api.coinpaprika.com/v1/tickers"

def fetch_and_store_coinpaprika():
    db = SessionLocal()

    # 🔁 INCREMENTAL CHECK
    existing = db.query(RawCryptoData).filter_by(source="coinpaprika").first()
    if existing:
        logging.info("CoinPaprika data already ingested. Skipping.")
        db.close()
        return

    response = requests.get(COINPAPRIKA_URL, timeout=10)
    response.raise_for_status()

    data = response.json()
    logging.info(f"Fetched {len(data)} records from CoinPaprika")

    try:
        record = RawCryptoData(
            source="coinpaprika",
            data=data
        )
        db.add(record)
        db.commit()
        logging.info("CoinPaprika data stored successfully")
    except Exception as e:
        db.rollback()
        logging.error(f"DB error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    fetch_and_store_coinpaprika()
