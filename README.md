# 🌦️ Weather Data Pipeline  
A real-time **data engineering pipeline** built using **Apache Airflow, WeatherStack API, PostgreSQL, DBT, Docker, and Apache Superset**.  
The pipeline automatically **extracts live weather data**, transforms it, loads it into a Postgres database, and visualizes it through interactive dashboards.

---

##  Project Overview
This project demonstrates a **complete end-to-end data pipeline** designed for real-time weather monitoring.  
It automates the entire workflow:

1. **Extract** weather data from WeatherStack API  
2. **Load** the raw data into PostgreSQL  
3. **Transform** the data using **DBT (Data Build Tool)**  
4. **Schedule & orchestrate** the workflow using **Apache Airflow**  
5. **Containerize** everything using Docker  
6. **Visualize** the processed data in **Apache Superset**

This project reflects real-world data engineering concepts such as:  
✔ ETL pipelines  
✔ Scheduling & automation  
✔ Database design  
✔ Containerization  
✔ Data transformation  
✔ Dashboarding  

---


---

##  Technologies Used

| Component | Technology |
|----------|------------|
| Orchestration | Apache Airflow |
| Data Source | WeatherStack API |
| Database | PostgreSQL |
| Transformations | DBT |
| Dashboard | Apache Superset |
| Containerization | Docker & Docker Compose |
| Scripting | Python |

---

##  Project Structure
```

weather-data-project/
│
├── airflow/
│   └── dags/
│       └── orchestrator.py       # Airflow DAG (The Pipeline Blueprint)
├── api-request/
│   ├── api_request.py          # Python: Fetches data from WeatherStack API
│   └── insert_records.py       # Python: Loads raw data into Postgres
├── dbt/
│   └── my_project/             # DBT Transformation Models (SQL & Jinja)
├── postgres/
│   ├── airflow_init.sql          # DB setup for Airflow metadata
│   └── superset_init.sql         # DB initialization for Superset access
├── docker-compose.yaml         # Defines all services (Airflow, Postgres, Superset, etc.)
└── .env (ignored)              # Secret API Key and other environment variables
```

##  How It Works

### **1. Extract Data**
A Python script (`api_request.py`) calls the **WeatherStack API** and fetches:

- Temperature  
- Humidity  
- Wind speed  
- Local time  
- Weather description  
- Location details  

The data is stored in a JSON structure and passed to Airflow.

---

### **2. Load Data**
Airflow triggers `insert_records.py` to insert raw weather data into PostgreSQL.

---

### **3. Transform Data (DBT)**
DBT performs:

- Data cleaning  
- Creating staging models  
- Aggregation of temperature & humidity  
- Daily weather summary  
- Materialized marts for dashboards  

---

### **4. Visualize Data (Superset)**
Superset connects to PostgreSQL and displays dashboards such as:

- Temperature changes over time  
- Humidity levels  
- Wind speed analysis  
- Summary reports  

---

##  Run the Project

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/Ask2meer/weather-data-pipeline.git
cd weather-data-pipeline
```
### 👤 Author

- Meer Abdullah (Ask2meer)
- Data Engineering & Python Developer
- GitHub: https://github.com/Ask2meer


