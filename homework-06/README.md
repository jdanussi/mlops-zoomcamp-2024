# Homework 06

### Follow these steps to run the unit and integration tests

```bash
# Clon the repository
git clone https://github.com/jdanussi/mlops-zoomcamp-2024.git

# Install dependencies
cd mlops-zoomcamp-2024/homework-06
pipenv install

# Run the test
cd mlops-zoomcamp-2024/homework-06/integration_test
chmod +x run.sh
./run.sh
```

Below is an example of the command output

```bash
> ./run.sh 
Running unit tests...

Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
============================================================= test session starts =============================================================
platform linux -- Python 3.10.12, pytest-8.2.2, pluggy-1.5.0
rootdir: /home/jdanussi/Documents/DataTalksClub/mlops-zoomcamp/mlops-zoomcamp-2024/homework-06
collected 1 item                                                                                                                              

../tests/test_batch.py .                                                                                                                [100%]

============================================================== 1 passed in 0.42s ==============================================================
Running integration test...

[+] Building 0.0s (0/0)                                                                                                         docker:default
[+] Running 2/2
 ✔ Network integration_test_default         Created                                                                                       0.1s 
 ✔ Container integration_test-localstack-1  Started                                                                                       0.1s 
make_bucket: nyc-duration
2024-07-03 23:59:53 nyc-duration
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
predicted mean duration: 18.138625226015364
predicted sum duration: 36.27725045203073
2024-07-03 23:59:55       3620 yellow_tripdata_2023-01.parquet
[+] Running 2/2
 ✔ Container integration_test-localstack-1  Removed                                                                                       3.8s 
 ✔ Network integration_test_default         Removed                                                                                       0.4s 
> 
```
