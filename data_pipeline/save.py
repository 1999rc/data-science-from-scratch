import os 
import logging 
def save_to_csv(df,output_dir='output'):
    filename='data.csv'
    os.makedirs(output_dir,exist_ok=True)
    path=os.path.join(output_dir,filename)
    df.to_csv(path,index=False)
    logging.info(f'Saved data to {path}')