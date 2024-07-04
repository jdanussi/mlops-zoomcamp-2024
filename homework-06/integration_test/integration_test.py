
import os
import subprocess
from datetime import datetime
import pandas as pd



def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)


def save_data(data, output_file):
    
    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df_input = pd.DataFrame(data, columns=columns)

    options = {
        'client_kwargs': {
            'endpoint_url': os.getenv('S3_ENDPOINT_URL')
        }
    }
    
    df_input.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )    



if __name__ == '__main__':
    
    # creating the fake data
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]
    
    output_file = 's3://nyc-duration/trip-data/yellow_tripdata_2023-01.parquet'
    
    save_data(data, output_file)

    # Get the parent directory
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Change to the parent directory
    os.chdir(parent_directory)

    # Run batch.py
    subprocess.run(["python", "batch.py", "2023", "1"])