import pandas as pd
from sqlalchemy import create_engine

csv_path = "radio_tracks_clean.csv"

df = pd.read_csv(csv_path)
df.columns = ["played_at", "title", "duration", "content_type"]

df["played_at"] = df["played_at"].astype(str).str.lstrip("s")
df["duration"] = pd.to_numeric(df["duration"], errors="coerce")

user = "root"
password = "admin"
host = "localhost"
port = 3306
database = "radiostation_database"

connection_string = (
    f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
)

engine = create_engine(connection_string)
table_name = "radio_data"

df.to_sql(
    name=table_name,
    con=engine,
    if_exists="append",
    index=False
)