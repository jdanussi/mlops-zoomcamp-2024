#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import pyarrow

categorical = ['PULocationID', 'DOLocationID']


def read_data(filename, year, month):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    # Add ride_id to DataFrame
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    
    return df


def apply_model(df):

    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
   
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    
    df_result = pd.DataFrame()
    df_result['ide_id'] = df['ride_id']
    df_result['predictions'] = y_pred
    
    return df_result


def output_to_parquet(df, output_file):
    df_result = df
    
    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )
    

if __name__ == "__main__":
        
    year = 2023
    month = 5

    url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f'output/df_results_yellow_tripdata_{year:04d}-{month:02d}.parquet'
    
    df = read_data(url, year, month)
    df_result = apply_model(df)
    output_to_parquet(df_result, output_file)
    
    mean_prediction = df_result['predictions'].mean()
    print("Mean predicted value:", mean_prediction)
    
    