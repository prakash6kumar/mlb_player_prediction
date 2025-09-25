import pandas as pd
import psycopg
from dotenv import load_dotenv
import os

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
csv_file = os.path.join(BASE_DIR, "..", "data", "cleaned", "batting_clean.csv")
df = pd.read_csv(csv_file)

create_table_query = """
CREATE TABLE IF NOT EXISTS batting (
    playerid   VARCHAR(20),
    yearid     INT,
    teamid     VARCHAR(10),
    ab         INT,
    r          INT,
    h          INT,
    "2b"       INT,
    "3b"       INT,
    hr         INT,
    rbi        INT,
    sb         INT,
    bb         INT,
    so         INT,
    hbp        INT,
    sf         INT,
    "1b"       INT,
    avg        NUMERIC(5,3),
    obp        NUMERIC(5,3),
    slg        NUMERIC(5,3),
    babip      NUMERIC(5,3),
    iso        NUMERIC(5,3),
    bb_pct     NUMERIC(5,3),
    k_pct      NUMERIC(5,3),
    xbh_pct    NUMERIC(5,3)
);
"""
with conn.cursor() as cur:
    cur.execute(create_table_query)
    conn.commit()

copy_sql = """
COPY batting(
    playerid, yearid, teamid, ab, r, h,"2b", "3b", hr, rbi,
    sb, bb, so, hbp, sf, "1b", avg, obp, slg, babip, iso,
    bb_pct, k_pct, xbh_pct
)
FROM STDIN WITH CSV HEADER
"""

with conn.cursor() as cur:
    with open(csv_file, "r") as f:
        with cur.copy(copy_sql) as copy:
            for line in f:
                copy.write(line)
    conn.commit()

   
    cur.execute("SELECT * FROM batting LIMIT 10;")   
    rows = cur.fetchall()                            
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    df = df.astype({col: float for col in ['avg','obp','slg','babip','iso','bb_pct','k_pct','xbh_pct']})
    print(df.head(10))

conn.close()