import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

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
        
        target = 'duration'
        y_train = df[target].values
        
        model = LinearRegression()
        model.fit(X_train, y_train)

        print('Intercept Value: ', model.intercept_)

        mlflow.sklearn.log_model(model, artifact_path="models")

        return X_train, model

