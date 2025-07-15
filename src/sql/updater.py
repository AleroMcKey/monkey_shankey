import pandas as pd
from sqlalchemy import create_engine

def load_sql_data(connection_string, query):
    sql_string = "sql"
    connection_string = "connection string"
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)
    return df
