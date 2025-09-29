import pandas as pd
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

conn = psycopg.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
) 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sql_file = os.path.join(BASE_DIR,"..","sql","feature_queries.sql")

with open(sql_file, "r") as f:
    feature_query = f.read()
df = pd.read_sql(feature_query,conn)

numeric_cols = ['avg','obp','slg','babip','iso','bb_pct','k_pct','xbh_pct',
                'bb_k_ratio','contact_rate','hr_rate','xbh_rate','rbi_rate',
                'runs_created','sb_rate','singles_pct']

df[numeric_cols] = df[numeric_cols].astype(float)
print(df.head(15))
print(df.info)

processed_path = os.path.join(BASE_DIR,"..","data","cleaned","ml_feautres.csv")
df.to_csv(processed_path,index=False)

conn.close()

