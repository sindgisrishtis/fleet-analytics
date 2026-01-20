import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/vehicle_telematics.csv")

# Basic validation
df = df[df["distance_km"] > 0]
df = df[df["fuel_liters"] > 0]

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Feature engineering
df["fuel_efficiency"] = df["distance_km"] / df["fuel_liters"]

# Save cleaned data
df.to_csv("data/cleaned/vehicle_telematics_clean.csv", index=False)

print("Cleaned vehicle telematics data created.")
