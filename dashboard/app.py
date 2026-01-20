import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Fleet Analytics Dashboard", layout="wide")

st.title("🚗 Fleet Telematics Dashboard")

# Connect to SQLite database
conn = sqlite3.connect("database/fleet.db")
df = pd.read_sql("SELECT * FROM fleet_data", conn)

# Sidebar filter
st.sidebar.header("Filters")
vehicle_ids = df["vehicle_id"].unique()
selected_vehicle = st.sidebar.selectbox(
    "Select Vehicle ID",
    options=["All"] + list(vehicle_ids)
)

if selected_vehicle != "All":
    df = df[df["vehicle_id"] == selected_vehicle]

# KPI Section
st.subheader("📊 Fleet KPIs")

kpis = df.groupby("vehicle_id").agg(
    total_distance=("distance_km", "sum"),
    avg_fuel_efficiency=("fuel_efficiency", "mean"),
    avg_engine_temp=("engine_temp", "mean"),
    error_days=("error_code", "sum")
).reset_index()

st.dataframe(kpis)

df["maintenance_alert"] = (
    (df["engine_temp"] > 100) |
    (df["error_code"] == 1)
).astype(int)


# Maintenance Alerts
st.subheader("🚨 Maintenance Alerts")

alerts = df[df["maintenance_alert"] == 1]
st.write(f"Total Alerts: {len(alerts)}")
st.dataframe(alerts.head())

# Visualization
st.subheader("📈 Average Fuel Efficiency per Vehicle")
st.bar_chart(
    df.groupby("vehicle_id")["fuel_efficiency"].mean()
)
