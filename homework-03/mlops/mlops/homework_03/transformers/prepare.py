import pandas as pd

from mlops.utils.data_preparation.cleaning_yellow import read_dataframe

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(df: pd.DataFrame) -> pd.DataFrame:

    df = read_dataframe(df)

    return df