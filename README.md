# NYC Taxi Data Pipeline

A beginner ETL pipeline that extracts, cleans, and loads 2.8 million NYC Yellow Taxi trips into a PostgreSQL database using Python and Pandas.

## Pipeline Architecture

```
Raw Parquet → Extract → Transform → Load → PostgreSQL
```

## Tools Used

- Python 3.13
- Pandas
- SQLAlchemy
- PostgreSQL 18
- pyarrow

## How to Run

1. Clone the repository
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Create a `.env` file with your database connection:
```
   DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taxidb
```
4. Create the database table:
```bash
   psql -U postgres -d taxidb -f sql/create_table.sql
```
5. Run the pipeline:
```bash
   python main.py
```

## Dataset

- Source: NYC Taxi & Limousine Commission
- File: yellow_tripdata_2023-01.parquet
- Raw rows: 3,066,766
- Clean rows after transformation: 2,884,216

## Data Cleaning Steps

- Removed rows with null values
- Removed trips with zero or negative distance
- Removed trips with zero or negative fare
- Removed trips with invalid passenger counts (outside 1-6)

## Results & Insights

### Busiest Pickup Hours
| Hour | Trip Count |
|------|------------|
| 18 (6PM) | 203,606 |
| 17 (5PM) | 197,225 |
| 15 (3PM) | 185,459 |
| 16 (4PM) | 184,671 |
| 19 (7PM) | 182,682 |

### Average Fare by Passenger Count
| Passengers | Avg Fare |
|------------|----------|
| 1 | $18.07 |
| 2 | $20.40 |
| 3 | $19.86 |
| 4 | $20.88 |
| 5 | $17.97 |
| 6 | $18.04 |

### Average Tip % by Payment Type
| Payment Type | Avg Tip % |
|--------------|-----------|
| 1 (Credit Card) | 26.0% |
| 2 (Cash) | 0.0% |
| 3 (No Charge) | 0.0% |
| 4 (Dispute) | 0.1% |

## What I'd Add Next

- Schedule pipeline with Apache Airflow
- Add logging to a file instead of just the terminal
- Load multiple months of data
- Add data visualizations with Matplotlib