import pandas as pd 
def transform_data(df:pd.DataFrame)->pd.DataFrame:
    """
    Transform data into ML-ready format 
    """
    print("[TRANSFORM] Transforming data...")

    #example;standardize columns names
    df.columns=[col.lower().strip().replace("","_")
    for col in df.columns]
    
    print("[TRANSFORM] Transformation complete!")
    return df 