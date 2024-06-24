# Homework 05

## Follow these steps to see the dashboards and reports

```bash
git clone https://github.com/jdanussi/mlops-zoomcamp-2024.git
cd mlops-zoomcamp-2024/homework-05

conda create -n "venv-homework-05" python=3.11
conda activate venv-homework-05
pip install -r requirements.txt

# Create test database and table dummy_metrics. Populate the table with some data
python dummy_metrics_calculation.py

# Create the table evidently_metrics. Populate the table with some metrics for March 2024 Green Taxi data
python evidently_metrics_calculation.py

# See the saved dashboards in Grafana
docker compose up --build

# and open Grafana from http://localhost:3000

# See the dashboard and regular reports in Evidently UI
# 1) Run all the notebook  baseline_model_nyc_taxi_data.ipynb 
evidently ui

# and open Evidently UI from http://localhost:8000
```
