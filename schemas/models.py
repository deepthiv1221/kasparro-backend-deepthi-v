from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class RawCryptoData(Base):
    __tablename__ = "raw_crypto_data"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
