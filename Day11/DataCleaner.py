import pandas as pd
import numpy as np
class DataCleaner:
    def __init__(self,numeric_fill='mean',categorical_fill='mode',date_columns=None,z_thresh=3):
        self.numerical_fill=numeric_fill
        self.categorical_fill=categorical_fill
        self.date_columns=date_columns
        self.z_thresh=z_thresh
    def clean(self,df:pd.DataFrame) -> pd.DataFrame:
        df=self.handle_missing(df)
        df=self.convert_data(df)
        df=self.remove_outliers(df)
        return df
    def handle_missing(self,df:pd.DataFrame) -> pd.DataFrame:
        for col in df.select_dtypes(include=np.number).columns:
            if self.numerical_fill=='mean':
                df[col]=df[col].fillna(df[col].mean())
            elif self.numerical_fill=='median':
                df[col]=df[col].fillna(df[col].median())
            elif isinstance(self.numerical_fill, (int, float)):
                df[col]=df[col].fillna(self.numerical_fill)
        for col in df.select_dtypes(include='object').columns:
            if self.categorical_fill=='mode':
                df[col]=df[col].fillna(df[col].mode()[0])
            elif isinstance(self.categorical_fill,str):
                df[col]=df[col].fillna(self.categorical_fill)
        return df
    def convert_data(self,df:pd.DataFrame) ->pd.DataFrame:
        for col in self.date_columns:
            if col in df.columns:
                df[col]=pd.DataFrame(df[col],errors='coerce')
        return df
    def remove_outliers(self,df:pd.DataFrame) -> pd.DataFrame:
        numeric_cols=df.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            mean,std=df[col].mean(),df[col].std()
            z_score=(df[col]-mean)/std
            df=df[z_score.abs()<=self.z_thresh]
        return df
if __name__=='__main__':
    df=pd.read_csv('Sampledata.csv')
    cleaner=DataCleaner(date_columns=['Date'])
    clean_df=cleaner.clean(df)
    clean_df.to_csv("clean.csv",index=False)
    print(clean_df)