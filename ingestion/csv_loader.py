import csv
from core.db import SessionLocal
from core.models import NormalizedCrypto
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def load_csv():
    db = SessionLocal()
    try:
        with open("data/sample_crypto.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = NormalizedCrypto(
                    source="csv",
                    symbol=row["symbol"],
                    name=row["name"],
                    price=float(row["price"]),
                    fetched_at=datetime.utcnow()
                )
                db.add(record)
        db.commit()
        logging.info("CSV data ingested successfully")
    except Exception as e:
        db.rollback()
        logging.error(f"CSV ingestion failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    load_csv()
