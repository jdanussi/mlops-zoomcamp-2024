# Homework 04

## Follow the steps to run the containerized python script `starter_v2.py`

```bash
git clone https://github.com/jdanussi/mlops-zoomcamp-2024.git
cd mlops-zoomcamp-2024/homework-04

docker build -t homework-04:v1 .
docker run -it --rm -v ./output:/app/output homework-04:v1 2023 05
```
