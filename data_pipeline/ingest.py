import pandas as pd 
def ingest_data(path:str)->pd.DataFrame:
    """
    Load raw data from CSV file
    """
    df=pd.read_csv(path)
    print(f"[INGEST]Data loaded with shape:{df.shape}")
    return df 
    