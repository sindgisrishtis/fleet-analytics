import pandas as pd
import random
from datetime import datetime, timedelta

records = []

for vehicle_id in range(1, 11):
    start_date = datetime(2024, 1, 1)

    for day in range(30):
        record = {
            "vehicle_id": vehicle_id,
            "date": start_date + timedelta(days=day),
            "distance_km": round(random.uniform(50, 300), 2),
            "fuel_liters": round(random.uniform(5, 25), 2),
            "engine_temp": round(random.uniform(70, 110), 2),
            "avg_speed": round(random.uniform(40, 90), 2),
            "error_code": random.choice([0, 0, 0, 1])
        }
        records.append(record)

df = pd.DataFrame(records)

df.to_csv("data/raw/vehicle_telematics.csv", index=False)

print("Raw vehicle telematics data created.")
