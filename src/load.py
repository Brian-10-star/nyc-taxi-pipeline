from sqlalchemy import create_engine
import pandas as pd

def load(df: pd.DataFrame, conn_string: str, table: str = "taxi_trips") -> None:
    print(f"[Load] Connecting to database...")
    engine = create_engine(conn_string)

    df.to_sql(
        name=table,
        con=engine,
        if_exists='append',
        index=False,
        chunksize=10_000
    )
    print(f"[Load] {len(df):,} rows written to '{table}'")