# Fleet Performance & Telematics Data Pipeline

## Project Overview
This project implements a backend data pipeline for fleet telematics analytics.
It covers synthetic data generation, data cleaning, feature engineering, and
loading data into a relational database.

## My Role (Backend Data Engineering)
- Designed project structure and data pipeline
- Generated synthetic telematics data
- Cleaned and validated raw data
- Engineered fuel efficiency metric
- Integrated processed data into SQLite database

## Tech Stack
- Python
- Pandas
- SQLite
- VS Code
- Jupyter (sanity checks only)

## How to Run
```bash
python etl/generate_data.py
python etl/clean_data.py
python etl/load_to_db.py
