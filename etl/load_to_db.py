import sqlite3
import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned/vehicle_telematics_clean.csv")

# Connect to SQLite database
conn = sqlite3.connect("database/fleet.db")

# Load data into table
df.to_sql("fleet_data", conn, if_exists="replace", index=False)

conn.close()

print("Data successfully loaded into SQLite database.")
