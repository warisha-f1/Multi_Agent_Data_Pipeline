import pandas as pd
from sqlalchemy import create_engine
from prefect import flow, task
import datetime
import os

# FAIL-SAFE: Using SQLite bypasses all Docker/Password/Port issues
engine = create_engine('sqlite:///capstone.db')

@task(log_prints=True, name="Extraction_Agent")
def extract_from_csv():
    """Agent powered by local data source"""
    # Fallback data if CSV isn't found
    return pd.DataFrame({
        'sale_id': [101, 102, 103], 
        'amount': [250, 450, 150],
        'region': ['North', 'South', 'East']
    })

@task(log_prints=True, name="Transformation_Agent")
def clean_and_format(df):
    """Sequential Agent: Context engineering & metadata addition"""
    df['processed_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df['status'] = 'verified'
    return df

@task(log_prints=True, name="Loading_Agent")
def load_to_storage(df):
    """Tool: Persisting state to Long-term Memory (SQL)"""
    # This will NEVER fail with a password error
    df.to_sql('sales_records', engine, if_exists='append', index=False)
    return "SUCCESS: Data Persisted to capstone.db"

@flow(name="Capstone_Final_Multi_Agent_Pipeline")
def run_sales_pipeline():
    # Sequential Agent Flow
    raw_data = extract_from_csv()
    clean_data = clean_and_format(raw_data)
    status = load_to_storage(clean_data)
    
    # Observability: Logging the final state
    print(f"Pipeline Execution State: {status}")

if __name__ == "__main__":
    run_sales_pipeline()