## 🚀 Overview
A resilient, multi-agent system designed to automate the Extraction, Transformation, and Loading (ETL) of sales data with built-in observability and state management.

## 🧠 System Architecture
The pipeline is orchestrated by **Prefect** and consists of three specialized agents:
1. **Extraction_Agent**: Pulls raw data from local source files.
2. **Transformation_Agent**: Performs context engineering, adding 'verified' status and 'processed_at' timestamps.
3. **Loading_Agent**: Persists the final state to a SQL Long-Term Memory (SQLite).

## 🛠️ Tech Stack
- **Orchestration**: Prefect (Logging & Tracing).
- **Database**: SQLite (Persistent State Management).
- **Data Handling**: Pandas & SQLAlchemy.

## 🔧 Problem Solving (Infrastructure Resilience)
During development, the system encountered `OperationalError` and `Database malformed` issues.
- **Resolution**: Implemented a "Clean-Start" protocol, clearing malformed binary states and re-provisioning the database engine to ensure 100% data integrity.

1. Environment Initialization
Ensure all dependencies for the agents, orchestration, and database engine are installed.

Bash

pip install prefect pandas sqlalchemy
2. Pipeline Execution
Trigger the Sequential Multi-Agent Flow. This starts the Prefect engine and executes the agents in order.

Bash

python sales_pipeline.py
3. Data Verification
Run the verification script to query the Long-Term Memory (SQL) and display the final enriched data.

Bash

python print_results.py
