from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 2,
        'title': 'Frontend Enginner',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Team Leader',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
]

@app.route('/')
def hello_world():
    return render_template(
        'home.html',
        company_name="Elegant Careers",
        jobs=JOBS
    )

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/1/')
def one():
    return 'doopa!'

@app.route('/2/')
def two():
    return 'doopa!'

@app.route('/3/')
def three():
    return 'doopa!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
