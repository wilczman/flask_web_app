from flask import Flask, render_template, jsonify
from sqlalchemy import text

from database import engine

app = Flask(__name__)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_dicts = []
        for row in result.mappings().all()():
            result_dicts.append(dict(row))
        return result_dicts

@app.route('/')
def hello_world():
    jobs = load_jobs_from_db()
    return render_template(
        'home.html',
        company_name="Elegant Careers",
        jobs=jobs,
    )

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

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
