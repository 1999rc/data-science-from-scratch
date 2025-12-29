import pandas as pd 
from data_pipeline.clean import clean_data 
def test_clean_data_removes_nulls():
    df=pd.DataFrame({
        "age":[25,None,30],
        "salary":[50000,60000,None]
    })
    cleaned_df=clean_data(df)
    assert cleaned_df.isnull().sum().sum()==0