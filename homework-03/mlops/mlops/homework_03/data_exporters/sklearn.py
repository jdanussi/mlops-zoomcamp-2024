import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

import pickle
import mlflow

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def train(df: pd.DataFrame):

    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("homework_03")

    with mlflow.start_run():

        mlflow.set_tag("developer", "Jorge Danussi")
            
        categorical = ['PULocationID', 'DOLocationID']
        train_dicts = df[categorical].to_dict(orient='records')

        dv = DictVectorizer()
        X_train = dv.fit_transform(train_dicts)
        
        # Save and log the DictVectorizer as an artifact
        with open("models/dv.pkl", "wb") as f_out:
            pickle.dump(dv, f_out)
        
        mlflow.log_artifact("models/dv.pkl", artifact_path="preprocessor")
        
        target = 'duration'
        y_train = df[target].values
        
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Log the model as an artifact
        mlflow.sklearn.log_model(model, artifact_path="models")

        print('Intercept Value: ', model.intercept_)
        mlflow.log_metric("intercept", model.intercept_)

        return X_train, model

