import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    print(f"[Extract] Reading file: {filepath}")
    df = pd.read_parquet(filepath)
    print(f"[Extract] Loaded {len(df):,} rows, {len(df.columns)} columns")
    return df