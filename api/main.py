from fastapi import FastAPI
from core.db import SessionLocal
from core.models import RawCryptoData

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/data")
def get_data():
    db = SessionLocal()
    try:
        latest = (
            db.query(RawCryptoData)
            .order_by(RawCryptoData.fetched_at.desc())
            .first()
        )

        if not latest:
            return {"message": "No data available"}

        return {
            "source": latest.source,
            "fetched_at": latest.fetched_at,
            "records": len(latest.data)
        }
    finally:
        db.close()

@app.get("/stats")
def stats():
    db = SessionLocal()
    try:
        total = db.query(RawCryptoData).count()
        return {
            "total_ingestion_runs": total,
            "status": "ok"
        }
    finally:
        db.close()
