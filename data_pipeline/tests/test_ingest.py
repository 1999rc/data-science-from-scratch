import pandas as pd 
from data_pipeline.ingest import ingest_csv
def test_ingest_csv_reads_file(tmp_path):
    #Create s temporary csv file 
    csv_file=tmp_path /"sample.csv"
    csv_file.write_text(
        "age,salary\n"
        "25,50000\n"
        "30,60000\n"
    )
    df=ingest_csv(csv_file)
    assert isinstance(df,pd.DataFrame)
    assert df.shape==(2,2)
    assert list(df.columns)==["age","salary"]
    