import pandas as pd

REQUIRED_COLUMNS = [
    'tpep_pickup_datetime', 'tpep_dropoff_datetime',
    'passenger_count', 'trip_distance',
    'fare_amount', 'tip_amount', 'total_amount', 'payment_type'
]

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("[Transform] Cleaning data...")

    df = df[REQUIRED_COLUMNS].copy()

    df.columns = [
        'pickup_datetime', 'dropoff_datetime',
        'passenger_count', 'trip_distance',
        'fare_amount', 'tip_amount', 'total_amount', 'payment_type'
    ]

    df['pickup_datetime']  = pd.to_datetime(df['pickup_datetime'],  errors='coerce')
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'], errors='coerce')

    df = df.dropna()
    df = df[df['trip_distance'] > 0]
    df = df[df['fare_amount']   > 0]
    df = df[df['passenger_count'].between(1, 6)]

    print(f"[Transform] {len(df):,} clean rows ready")
    return df