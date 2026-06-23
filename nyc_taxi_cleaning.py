# NYC Taxi Trips Cleaning - Internship Project
# Author: Aman
# Date: June 2026

import pandas as pd

# Step 1: Load Data
df = pd.read_csv("nyc_taxi.csv")
print("Initial Shape:", df.shape)

# Step 2: Deduplication
print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())

# Step 3: Handle Missing Values
print("Missing values:\n", df.isna().sum())

# Fill missing passenger_count with median
if "passenger_count" in df.columns:
    df["passenger_count"].fillna(df["passenger_count"].median(), inplace=True)

# Drop rows with missing trip_id
df.dropna(subset=["trip_id"], inplace=True)

# Step 4: Date Standardization
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce")
df["dropoff_datetime"] = pd.to_datetime(df["dropoff_datetime"], errors="coerce")

# Step 5: GPS Coordinate Cleaning
def validate_lat(lat):
    try:
        return lat if -90 <= float(lat) <= 90 else None
    except:
        return None

def validate_lon(lon):
    try:
        return lon if -180 <= float(lon) <= 180 else None
    except:
        return None

df["pickup_latitude"] = df["pickup_latitude"].apply(validate_lat)
df["pickup_longitude"] = df["pickup_longitude"].apply(validate_lon)
df["dropoff_latitude"] = df["dropoff_latitude"].apply(validate_lat)
df["dropoff_longitude"] = df["dropoff_longitude"].apply(validate_lon)

# Step 6: Fare Cleaning
df = df[df["fare_amount"] > 0]   # remove negative/zero fares
df = df[df["fare_amount"] < 500] # remove unrealistic fares

# Step 7: Validation
assert df["trip_id"].isna().sum() == 0
assert df.duplicated().sum() == 0

# Step 8: Save Cleaned File
df.to_csv("cleaned_nyc_taxi.csv", index=False)
print("✅ Cleaned dataset saved as cleaned_nyc_taxi.csv")
