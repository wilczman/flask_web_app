from flask import Flask, render_template, jsonify, request

from database import add_calculation_to_db

from price_calculator import calculate_price


app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'home.html',
        company_name="Dwa Smyczki",
    )

@app.route('/posluchaj')
def posluchaj():
    return render_template('listen.html')

@app.route('/oferta')
def oferta():
    return render_template('oferta.html')

@app.route('/cennik')
def cennik():
    return render_template('cennik.html')

@app.route("/cennik/oblicz", methods=['post'])
def apply_to_job():
    data = request.form
    calculation = calculate_price(data['place'], data['postal_code'])
    # add_calculation_to_db(id, data)
    return render_template(
        'cennik.html',
        calculation=calculation,
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
