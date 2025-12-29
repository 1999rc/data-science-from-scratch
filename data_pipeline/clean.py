import pandas as pd 
def clean_data(df:pd.DataFrame)->pd.DataFrame:
    """
    Handle missing values
    """
    print("[ClEAN] Cleaning data...")
    #full numeric columns with median 
    
    for col in df.select_dtypes(include='number').columns:
        df[col]=df[col].fillna(df[col].median())

    #Fill categorical columns with mode 
    for col in df.select_dtypes(include='object').columns:
        df[col]=df[col].fillna(df[col].mode()[0])
    print("[CLEAN] Missing values handled")
    return df 
