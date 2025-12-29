import logging 
import requests
import pandas as pd 
from bs4 import BeautifulSoup
logger=logging.getLogger(__name__)
def scrape_data():
    logger.info("Fetching data from web...")
    url="https://quotes.toscrape.com/"
    response=requests.get(url)
    if response.status_code!=200:
        raise Exception("Failed to fetch data")
    soup=BeautifulSoup(response.text,"html.parser")
    quotes=soup.find_all("span",class_="text")
    data={"quote":[q.text for q in quotes]}
    df=pd.DataFrame(data)

    logger.info(f"Collected {len(df)} rows")
    return df 