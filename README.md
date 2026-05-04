# NYC Taxi Data Pipeline

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-316192?logo=postgresql)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)
![ETL](https://img.shields.io/badge/Pipeline-ETL-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

An end-to-end ETL pipeline that ingests, cleans, and loads **3 million+ NYC Yellow Taxi trip records** into a PostgreSQL database using Python and Pandas. Built as the first project in a structured Data Engineering portfolio.

---

## Pipeline Architecture

```
NYC TLC Parquet File
        │
        ▼
┌───────────────┐
│    Extract    │  Read 3,066,766 rows from .parquet using pyarrow
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Transform   │  Clean data → remove nulls, invalid fares,
│               │  invalid distances, invalid passenger counts
└───────┬───────┘
        │
        ▼
┌───────────────┐
│     Load      │  Batch insert 10,000 rows at a time into PostgreSQL
└───────┬───────┘
        │
        ▼
  PostgreSQL DB
  taxidb → taxi_trips
  2,884,216 clean rows
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.13 | Pipeline logic |
| Pandas | Data transformation and cleaning |
| pyarrow | Reading Parquet files |
| SQLAlchemy | Database connection and batch loading |
| psycopg2 | PostgreSQL driver |
| python-dotenv | Secure credential management via .env |
| PostgreSQL 18 | Data storage |

---

## Dataset

- **Source:** NYC Taxi & Limousine Commission (TLC)
- **File:** `yellow_tripdata_2023-01.parquet`
- **Raw rows:** 3,066,766
- **Clean rows loaded:** 2,884,216
- **Rows removed:** 182,550 (~6%)

---

## Data Cleaning Logic

| Rule | Reason |
|---|---|
| Remove null values | Incomplete records unusable for analysis |
| Remove trips with distance ≤ 0 | Invalid — no movement recorded |
| Remove trips with fare ≤ 0 | Invalid — likely cancelled or corrupt entries |
| Remove passenger count outside 1–6 | Outside legal NYC taxi capacity |

---

## Results & Insights

### Busiest Pickup Hours
| Hour | Trip Count |
|---|---|
| 18 (6 PM) | 203,606 |
| 17 (5 PM) | 197,225 |
| 15 (3 PM) | 185,459 |
| 16 (4 PM) | 184,671 |
| 19 (7 PM) | 182,682 |

### Average Fare by Passenger Count
| Passengers | Avg Fare |
|---|---|
| 1 | $18.07 |
| 2 | $20.40 |
| 3 | $19.86 |
| 4 | $20.88 |
| 5 | $17.97 |
| 6 | $18.04 |

### Average Tip % by Payment Type
| Payment Type | Avg Tip % |
|---|---|
| 1 — Credit Card | 26.0% |
| 2 — Cash | 0.0% |
| 3 — No Charge | 0.0% |
| 4 — Dispute | 0.1% |

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Brian-10-star/nyc-taxi-pipeline.git
cd nyc-taxi-pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taxidb
```

### 4. Create the database table
```bash
psql -U postgres -d taxidb -f sql/create_table.sql
```

### 5. Run the pipeline
```bash
python main.py
```

---

## Project Portfolio

This is Project 1 of 5 in my Data Engineering portfolio. Each project builds on the last:

| # | Project | Tools |
|---|---|---|
| 1 | **NYC Taxi Pipeline** ← you are here | Python, Pandas, PostgreSQL |
| 2 | [Nairobi Weather Pipeline](https://github.com/Brian-10-star/weather-pipeline) | Python, REST API, PostgreSQL |
| 3 | [Airflow Weather DAG](https://github.com/Brian-10-star/weather-pipeline) | Apache Airflow, Cron, XCom |
| 4 | [dbt Data Warehouse](https://github.com/Brian-10-star/taxi-dbt) | dbt, SQL, Data Modeling |
| 5 | Cloud Pipeline | GCP, Cloud Storage, Cloud Functions |

---

## Author

**Brian Mbugua Chira**
BSc Computer Science — Egerton University, Kenya (Expected 2028)

- GitHub: [github.com/Brian-10-star](https://github.com/Brian-10-star)
- LinkedIn: [linkedin.com/in/mbuguabrian](https://linkedin.com/in/mbuguabrian)
- Email: chirabrian1@gmail.com
