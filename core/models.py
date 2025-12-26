from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class RawCryptoData(Base):
    __tablename__ = "raw_crypto_data"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    data = Column(JSON)
    fetched_at = Column(DateTime, default=datetime.utcnow)

class NormalizedCrypto(Base):
    __tablename__ = "normalized_crypto"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    symbol = Column(String)
    name = Column(String)
    price = Column(Float)
    fetched_at = Column(DateTime, default=datetime.utcnow)
