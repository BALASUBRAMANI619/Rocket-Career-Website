from flask import Flask,render_template,jsonify
from database import load_jobs_from_db
from sqlalchemy import text
app = Flask(__name__)
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


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)