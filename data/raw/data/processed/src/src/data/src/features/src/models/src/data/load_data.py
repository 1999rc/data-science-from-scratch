from pathlib import Path 
DATA_DIR=Path("data/raw")
def load_raw_data():
  """Load raw data from data/raw directory"""
  files=list(DATA_DIR.glob("*"))
  return files
             
