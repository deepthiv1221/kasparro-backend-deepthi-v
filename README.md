# Kasparro Backend & ETL Systems Assignment

## Overview

This project implements a **production-grade backend and ETL system** that ingests cryptocurrency market data from multiple external APIs, stores raw data in a PostgreSQL database, and exposes APIs to retrieve and inspect the ingested data.

The system is designed with **clean architecture, scalability, recovery logic, and real-world backend practices**, closely mirroring how backend data platforms are built in production environments.

---

## Key Features

* ✅ Multi-source data ingestion (CoinPaprika & CoinGecko)
* ✅ ETL pipelines with idempotency (no duplicate ingestion)
* ✅ PostgreSQL database (Dockerized)
* ✅ FastAPI backend with REST APIs
* ✅ Recovery & error-handling logic
* ✅ Clean, modular folder structure
* ✅ Ready for future transformations & scaling

---

## Architecture

```
External APIs
 ├── CoinPaprika
 └── CoinGecko
        ↓
ETL / Ingestion Layer
        ↓
PostgreSQL (Dockerized)
        ↓
FastAPI Backend
        ↓
REST APIs
```

---

## Tech Stack

* **Python 3.10+**
* **FastAPI** – API layer
* **PostgreSQL** – Database
* **SQLAlchemy** – ORM
* **Docker & Docker Compose** – Containerization
* **Requests** – External API calls

---

## Data Sources

* **CoinPaprika API**
* **CoinGecko API**

Both APIs are ingested through dedicated ETL scripts and stored in a **single raw data table** with metadata.

---

## Database Design

### Table: `raw_crypto_data`

| Column     | Type     | Description                               |
| ---------- | -------- | ----------------------------------------- |
| id         | Integer  | Primary key                               |
| source     | String   | Data source (`coinpaprika` / `coingecko`) |
| data       | JSON     | Raw API response                          |
| fetched_at | DateTime | Timestamp of ingestion                    |

### Design Rationale

* Stores **raw data first** (industry best practice)
* Enables future transformations without re-fetching APIs
* Maintains full auditability of ingested data

---

## ETL / Ingestion Logic

Each ingestion pipeline:

1. Fetches data from the external API
2. Checks if data from the same source already exists
3. Skips ingestion if already ingested (idempotency)
4. Stores raw JSON data with timestamp
5. Handles failures with rollback and logging

### Supported Pipelines

* `ingestion.coinpaprika`
* `ingestion.coingecko`

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Latest Crypto Data

```
GET /data
```

Response:

```json
{
  "source": "coinpaprika",
  "fetched_at": "2025-12-26T05:21:49",
  "data_count": 2000
}
```

---

### Statistics Endpoint

```
GET /stats
```

Returns aggregated information about stored datasets.

---

## Project Structure

```
kasparro-backend-deepthi-v/
├── api/
│   └── main.py
├── core/
│   ├── db.py
│   ├── init_db.py
│   └── models.py
├── ingestion/
│   ├── coinpaprika.py
│   ├── coingecko.py
│   └── csv_loader.py
├── schemas/
│   └── models.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/deepthiv1221/kasparro-backend-deepthi-v
cd kasparro-backend-deepthi-v
```

---

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\Activate.ps1       # Windows

pip install -r requirements.txt
```

---

### 3. Start PostgreSQL using Docker

```bash
docker-compose up -d
```

---

### 4. Initialize Database Tables

```bash
python -m core.init_db
```

---

### 5. Run ETL Pipelines

```bash
python -m ingestion.coinpaprika
python -m ingestion.coingecko
```

If data is already ingested, the pipeline safely skips execution.

---

### 6. Start API Server

```bash
uvicorn api.main:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

---

## Screenshots

### Health Check Endpoint

![WhatsApp Image 2025-12-26 at 11 37 01 PM](https://github.com/user-attachments/assets/4d446e6d-38d5-44bf-bad0-c707c356ffea)


---

### Crypto Data API

![WhatsApp Image 2025-12-26 at 11 36 51 PM](https://github.com/user-attachments/assets/1678388f-8a1b-4b15-b4df-77cbd686c417)


---

### Statistics Endpoint

![WhatsApp Image 2025-12-26 at 11 36 38 PM](https://github.com/user-attachments/assets/584ba40f-99cf-4d49-b0d1-5ffe4c4f5621)


---

## Engineering Considerations

* Clean separation of concerns
* Database-first design
* Idempotent ingestion
* Fault-tolerant ETL execution
* Dockerized infrastructure
* Easy extensibility for new data sources

---

## Future Improvements

* Scheduled ingestion (cron / Airflow)
* Data normalization layer
* Authentication & authorization
* Pagination & filtering APIs
* Monitoring & metrics

---

## Author

**Deepthi Vijay Kumar**
Backend & Data Engineering Assignment — Kasparro

---
