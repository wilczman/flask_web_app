from flask import Flask, render_template, jsonify, request

from database import load_jobs_from_db, load_specific_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template(
        'home.html',
        company_name="Dwa Smyczki",
        jobs=jobs,
    )

@app.route('/posluchaj')
def posluchaj():
    return render_template('listen.html')

@app.route('/oferta')
def oferta():
    return render_template('oferta.html')

@app.route('/cennik')
def cennik():
    return render_template('prices.html')

# @app.route('/api/jobs')
# def list_jobs():
#     jobs = load_jobs_from_db()
#     return jsonify(jobs)

# @app.route('/jobs/<id>')
# def show_job(id):
#     job = load_specific_job_from_db(id)
#     if not job:
#         return "Not Found", 404
#     else:
#         return render_template(
#             'jobpage.html',
#             job=job
#         )

# @app.route("/jobs/<id>/apply", methods=['post'])
# def apply_to_job(id):
#     data = request.form
#     job = load_specific_job_from_db(id)
#     add_application_to_db(id, data)
#     return render_template(
#         'application_submitted.html',
#         application=data
#     )

# @app.route('/api/jobs/<id>')
# def api_show_job(id):
#     job = load_specific_job_from_db(id)
#     return jsonify(job)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
