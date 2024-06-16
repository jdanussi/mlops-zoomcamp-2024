FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install -U pip
RUN pip install pipenv

# Folder for output processing
RUN mkdir -p /app/output

WORKDIR /app
COPY [ "Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY [ "starter_v2.py", "./"] 

ENTRYPOINT [ "python", "/app/starter_v2.py" ]