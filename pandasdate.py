import pandas as pd
import datetime as dt
import pyarrow
import numpy as np
import openpyxl

class DataFrame(pd.DataFrame):
    
    def __init__(self, *args, year:int=2000, month:int=9, day:int=19, **kwargs) -> None:
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.date:dt.date = dt.date(year=year, month=month, day=day)
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nDate: {self.date}" # For terminal print
    
    def _repr_html_(self) -> str:
        return f"{super()._repr_html_()}<br>Date: {self.date}" # For Jupyter Notebook rich display
    
    def to_csv(self, path:str) -> None:
        df:pd.DataFrame = self.copy()
        df['__date'] = self.date
        df.to_csv(path)
    
    def to_parquet(self, path:str) -> None:
        df:pd.DataFrame = self.copy()
        df['__date'] = self.date
        df.to_parquet(path)

    def to_excel(self, path:str) -> None:
        df:pd.DataFrame = self.copy()
        df['__date'] = self.date
        df.to_excel(path)

    def to_pickle(self, path:str) -> None:
        df:pd.DataFrame = self.copy()
        df['__date'] = self.date
        df.to_pickle(path)


def _reconstruct(df: pd.DataFrame) -> pd.DataFrame:
    date:dt.date = pd.to_datetime(df['__date']).dt.date.iloc[0]
    df:pd.DataFrame = df.drop(columns=['__date'])

    '''
    when reading csv and excel files,
    if they don't have a column name for the index,
    `unnamed: 0` will be asssigned by default.
    This effort is to alter this behavior
    to construct a meaningful dataframe.
    '''
    if df.columns[0] == 'Unnamed: 0':
        df:pd.DataFrame = df.set_index(df['Unnamed: 0'].values)
        df:pd.DataFrame = df.drop(columns=['Unnamed: 0'])

    new_df:pd.DataFrame = DataFrame(df)
    new_df.date = date
    return new_df

def read_csv(path:str) -> pd.DataFrame:
    df:pd.DataFrame = pd.read_csv(path)
    return _reconstruct(df)

def read_parquet(path:str) -> pd.DataFrame:
    df:pd.DataFrame = pd.read_parquet(path)
    return _reconstruct(df)

def read_excel(path:str) -> pd.DataFrame:
    df:pd.DataFrame = pd.read_excel(path)
    return _reconstruct(df)

def read_pickle(path:str) -> pd.DataFrame:
    df:pd.DataFrame = pd.read_pickle(path)
    return _reconstruct(df)