CREATE TABLE IF NOT EXISTS taxi_trips (
    trip_id         SERIAL PRIMARY KEY,
    pickup_datetime TIMESTAMP,
    dropoff_datetime TIMESTAMP,
    passenger_count INT,
    trip_distance   FLOAT,
    fare_amount     FLOAT,
    tip_amount      FLOAT,
    total_amount    FLOAT,
    payment_type    INT
);