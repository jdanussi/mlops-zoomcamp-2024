import pandas as pd

from mlops.homework_03.utils.cleaning import read_dataframe

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(df: pd.DataFrame) -> pd.DataFrame:

    df = read_dataframe(df)
    print(f'Dataframe total rows: {df.shape[0]}')

    return df