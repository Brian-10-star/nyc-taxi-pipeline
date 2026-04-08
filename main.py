import os
from dotenv import load_dotenv
from src.extract import extract
from src.transform import transform
from src.load import load

load_dotenv()

FILE_PATH = "data/raw/yellow_tripdata_2023-01.parquet"
DB_CONN   = os.getenv("DATABASE_URL")

if __name__ == "__main__":
    df = extract(FILE_PATH)
    df = transform(df)
    load(df, DB_CONN)
    print("Pipeline complete!")