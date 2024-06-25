# Homework 05

## Follow these steps to see the dashboards and reports

```bash
git clone https://github.com/jdanussi/mlops-zoomcamp-2024.git
cd mlops-zoomcamp-2024/homework-05

conda create -n "venv-homework-05" python=3.11
conda activate venv-homework-05
pip install -r requirements.txt

# Run the containers with the services
docker compose up --build

# Create test database and table dummy_metrics. Populate the table with some data
python dummy_metrics_calculation.py

# Create the table evidently_metrics. Populate the table with some metrics for March 2024 Green Taxi data
python evidently_metrics_calculation.py


# To see the saved dashboars in Grafana go to http://localhost:3000

# To see the savd dashboard and regular reports in Evidently UI run
evidently ui

# and open Evidently UI from http://localhost:8000
```
