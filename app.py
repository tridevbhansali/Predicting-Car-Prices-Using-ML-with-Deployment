from flask import Flask, render_template, request, jsonify
import numpy as np
import util

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('app.html')


@app.route("/brand_name")
def Brand_name():
    response_b = util.brand_name()
    response_b = jsonify(response_b)
    response_b.headers.add("Access-Control-Allow-Origin", "*")
    return response_b

@app.route("/model_name")
def Model_name():
    response_m = util.model_name()
    response_m = jsonify(response_m)
    response_m.headers.add("Access-Control-Allow-Origin", "*")
    return response_m

@app.route("/year")
def Year():
    response_y = util.year()
    response_y = jsonify(response_y)
    response_y.headers.add("Access-Control-Allow-Origin", "*")
    return response_y

@app.route("/car_predicted", methods=['POST'])
def car_price():
    year = request.form.get('year')
    comp = request.form.get('brand_name')
    mod = request.form.get('model_name')
    fuel = request.form.get('fuel')
    km = request.form.get('km')
    pre = np.around(util.car_predict(year,comp,mod,fuel,km),decimals=2)
    predict = jsonify(pre.tolist())
    predict.headers.add("Access-Control-Allow-Origin", "*")
    return predict

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)


