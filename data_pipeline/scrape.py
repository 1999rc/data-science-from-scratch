import requests
import pandas as pd 
from bs4 import BeautifulSoup 
def scrape_data():
    print(f"[SCRAPE] Fetching data from WEB...")
    url="https://quotes.toscrape.com/"
    response=requests.get(url)
    if response.status_code!=200:
        raise Exception("Failed to fetch data")
    soup=BeautifulSoup(response.text,"html.parser")
    quotes=soup.find_all("span",class_="text")
    data={"quote":[q.text for q in quotes]}
    df=pd.DataFrame(data)

    print(f"[SCRAPE] Colected {len(df)} rows")
    return df 