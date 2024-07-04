
from datetime import datetime
import pandas as pd
from pandas.testing import assert_frame_equal
from batch import read_data



def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)



def test_read_data():
    
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    current_data = pd.DataFrame(data, columns=columns)
    
    output_file = f'test_data.parquet'
    current_data.to_parquet(output_file, engine='pyarrow', index=False)
    
    expected_data = read_data(output_file)
    
    assert_frame_equal(current_data, expected_data, check_dtype=True)
