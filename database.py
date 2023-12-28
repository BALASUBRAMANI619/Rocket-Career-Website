
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

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val': id})
    
    row = result.fetchone()  # Use fetchone() instead of fetchall() for a single row
    if row is None:
        return None
    else:
        return dict(zip(result.keys(), row))
#        return dict(row)

def add_application_to_db(id, data):
  try:
      with engine.connect() as conn:
          query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
                       "VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

          # Combine job_id and data into a single dictionary
          params = {'job_id': id, **data}

          conn.execute(query, params)

          # Commit the changes
          conn.commit()
  except Exception as e:
      print(f"Error inserting data into the database: {e}")
