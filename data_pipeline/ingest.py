import logging 
import pandas as pd
logger=logging.getLogger(__name__) 
def ingest_csv(path):
    """
    READ a CSV and return a pandas DataFrame
    """
    return pd.read_csv(path)
def ingest_data(path:str)->pd.DataFrame:
    """
    Load raw data from CSV file
    """
    df=pd.read_csv(path)
    logger.ingo("Data loaded with shape: %s",df.shape)
    return df 
    