from flask import Flask,render_template,jsonify

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS)

@app.route('/API/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)