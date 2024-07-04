#!/usr/bin/env bash

# Unit Tests
echo "Running unit tests..."
echo 

pipenv run pytest ../tests


# Integration Test
echo "Running integration test..."
echo

docker compose up -d

sleep 5

export S3_ENDPOINT_URL="http://localhost:4566"
export S3_BUCKET_NAME="s3://nyc-duration"
export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"

aws --endpoint-url=http://localhost:4566 \
    s3 mb ${S3_BUCKET_NAME}

aws --endpoint-url=http://localhost:4566 s3 ls

pipenv run python integration_test.py

ERROR_CODE=$?

if [ ${ERROR_CODE} != 0 ]; then
    docker compose logs
    docker compose down
    exit ${ERROR_CODE}
fi

aws --endpoint-url=http://localhost:4566 \
    s3 ls ${S3_BUCKET_NAME}/trip-data/

docker compose down