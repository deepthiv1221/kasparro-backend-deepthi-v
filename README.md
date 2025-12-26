# Kasparro Backend & ETL Systems Assignment

## Overview
This project implements a production-style backend and ETL system that ingests cryptocurrency market data from multiple external sources, stores raw data in a PostgreSQL database, and exposes APIs to retrieve processed information.

The system is designed with modularity, scalability, and maintainability in mind, following real-world backend engineering practices.

---

## Architecture

External APIs
├── CoinPaprika
└── CoinGecko
↓
Ingestion Layer (ETL)
↓
PostgreSQL (Dockerized)
↓
FastAPI Backend


---

## Tech Stack
- **Python 3.10+**
- **FastAPI** – API layer
- **PostgreSQL** – Data storage
- **SQLAlchemy** – ORM
- **Docker & Docker Compose** – Containerization
- **Requests** – API calls

---

## Data Sources
- **CoinPaprika API**
- **CoinGecko API**

Both sources are ingested using the same ETL pipeline and stored in a unified database table with metadata.

---

## Database Design

### Table: `raw_crypto_data`

| Column       | Type     | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key |
| source      | String   | Data source (`coinpaprika` / `coingecko`) |
| data        | JSON     | Raw API response |
| fetched_at  | DateTime | Timestamp of ingestion |

This raw-data-first approach keeps the system flexible for future transformations.

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd kasparro-backend-deepthi-vijay-kumar

2. Create virtual environment & install dependencies

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

3. Start PostgreSQL using Docker

docker-compose up -d

4. Initialize database tables

python -m core.init_db

5. Run ingestion pipelines

python -m ingestion.coinpaprika
python -m ingestion.coingecko

6. Start the API server

uvicorn api.main:app --reload


