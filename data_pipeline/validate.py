import pandas as pd 
def validate_data(df:pd.DataFrame)->None:
    """
    Validate data for nulls and basic integrity
    """
    print("[VALIDATE] Checking missing values...")
    missing=df.isnull().sum()
    if missing.any():
        print("[VALIDATE] Missing values found;")
        print(missing)
    else:
        print("[VALIDATE] No missing values found")
        return df 