from sqlalchemy import Column, Integer, String, JSON, DateTime
from datetime import datetime
from core.db import Base   # 👈 THIS IS THE KEY FIX

class RawCryptoData(Base):
    __tablename__ = "raw_crypto_data"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    data = Column(JSON, nullable=False)
    fetched_at = Column(DateTime, default=datetime.utcnow)
