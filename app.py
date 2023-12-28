from flask import Flask,render_template,jsonify,request
from database import add_application_to_db, load_jobs_from_db, load_job_from_db

from sqlalchemy import text
app = Flask(__name__, static_url_path='/static')
'''
JOBS = [

    {
        'id':1,
        'title': 'System Administrator',
        'location': 'Mumbai, India',
        'salary': 'Rs 10,00,000'
    },
    {
        'id': 2,
        'title': 'Database Administrator',
        'location': 'Navi Mumbai, India',
        'salary': 'Rs 8,00,000'
    },
    {
        'id': 3,
        'title': 'Cloud Administrator',
        'location': 'Banglore, India',
        'salary': 'Rs 25,00,000'
    }
]
'''
@app.route('/')
def index():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route('/API/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route('/jobs/<id>')
def show_jobs(id):
    job = load_job_from_db(id)
    if job is None:
      return jsonify({'error': 'Job not found'}), 404
    return render_template('jobpage.html', job=job)

@app.route("/jobs/<id>/apply", methods=['POST'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                         application=data, job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)