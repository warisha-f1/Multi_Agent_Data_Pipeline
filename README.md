Project Overview:
This project implements a Sequential Multi-Agent System designed to handle automated data extraction, cleaning, and persistence. Built as a Capstone project, it demonstrates high-level State Management, Infrastructure Resilience, and Agent Observability.

The system is designed to recover from infrastructure failures, such as database corruption or authentication conflicts, ensuring 100% data integrity through automated recovery protocols.

System Architecture:
The pipeline utilizes a modular agent-based architecture orchestrated by Prefect.

Extraction Agent: A custom tool-powered agent that interfaces with raw data sources (CSV/Local).

Transformation Agent: An LLM-compatible sequential agent that performs context engineering and metadata enrichment.

Loading Agent: A long-term memory agent responsible for persisting state into a relational SQL database.

Tech Stack & Key Features:
Agent Framework: Prefect (for Logging, Tracing, and Flow Orchestration).

Database & State: SQLite (Production State) & PostgreSQL (Containerized Infrastructure).

State Management: InMemorySessionService logic for short-term state and SQL for Long-Term Memory (LTM).

Deployment: Docker Compose for containerized infrastructure.

Engineering Challenges & Resilience:
This project highlights real-world problem solving in Agent Deployment:

Network Resilience: Successfully resolved OperationalError by bypassing IPv6/IPv4 port conflicts (Port 5432/5433 migration).

State Recovery: Handled Database malformed exceptions by implementing a clean-slate re-provisioning protocol, ensuring the agent could recreate the persistent storage layer automatically.

Getting Started:
1. Environment Setup
Bash
pip install -r requirements.txt

2. Infrastructure (Optional)
To start the containerized Postgres database:
Bash
docker-compose up -d

3. Execution
Run the multi-agent pipeline:
Bash
python sales_pipeline.py

4. Verification (Observability)
View the persisted state and agent logs:
Bash
python print_results.py

Final Agent Output:
Upon successful execution, the agents verify the data persistence state as follows: | Sale ID | Amount | Region | Processed At | Status | | :--- | :--- | :--- | :--- | :--- | | 101 | 250 | North | 2025-12-28 17:07:15 | verified | | 102 | 450 | South | 2025-12-28 17:07:15 | verified | | 103 | 150 | East | 2025-12-28 17:07:15 | verified |
