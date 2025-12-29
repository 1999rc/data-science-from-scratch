from data_pipeline.ingest import ingest_data 
from data_pipeline.validate import validate_data
from data_pipeline.clean import clean_data
from data_pipeline.transform import transform_data
from data_pipeline.save import save_to_csv
from data_pipeline.scrape import scrape_data
import os
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    
    handlers=[
        logging.StreamHandler(), #console
        logging.FileHandler("pipeline.log") 
       
    ]
) 
logger=logging.getLogger(__name__)
def save_to_csv(df,output_dir="output",filename="quotes.csv"):
    #output_dir="output"
    os.makedirs(output_dir,exist_ok=True)

    filepath=os.path.join(output_dir,filename)
    df.to_csv("output/final_output.csv",index=False)
    logger.info("[SAVED] Data to %s",filepath)
    #print(f"[SAVE] Data saved to {filepath}")
def run_pipeline(source="csv",data_path=None):
    logger.info("PIPELINE STARTED...")
    if source=="scrape":
        df=scrape_data()
    else:
        df=ingest_data(data_path)

    #2 Validate 
    validate_data(df)

    #3 Clean 
    df=clean_data(df)

    #4 Transform 
    df=transform_data(df)

    save_to_csv(df)

    logger.info("PIPELINE FINISHED")
    return df
    #print(" PIPELINE FINISHED\n")
    logger.info("[SCRAPE] Collected %d rows",len(df))
    #logger.info("PIPELINE STARTED")
    #logger.info("PIPELINE FINISHED")

    #logger.info("[SAVED] Data saved to %s",filepath)
    logger.info("[VALIDATE] Cheking missing values...")

    logger.info("[VALIDATE] No missing values found!]")
    logger.info("[CLEAN] Cleaning data...")

    logger.info("[CLEAN] Missing values handled!")
    logger.info("[TRANSFORM] Transforming data...")
    logger.info("[TRANSFORM] Transformation complete!")
    #return df
'''try:
    run_pipeline(source="scrape")
except Exception as e:
    logger.exception('Pipeline failed!')'''
    #return df 
if __name__=='__main__':
   try:


    run_pipeline(source="scrape")
   except Exception as e:
    logger.exception('Pipeline failed!')
    #example path (change later)
    #run_pipeline(source="scrape")