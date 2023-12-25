
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    data = result.fetchall()
    column_names = result.keys()
  jobs = [dict(zip(column_names, row)) for row in data]
  return jobs