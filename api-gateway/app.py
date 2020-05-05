from flask import Flask, request, Response

import json
import os
import requests

app = Flask(__name__)

ADDITION_SERVICE_URL = os.environ.get('ADDITION_SERVICE_URL') or 'http://localhost:3000/addition'
MULTIPLICATION_SERVICE_URL = os.environ.get('MULTIPLICATION_SERVICE_URL') or 'http://localhost:3001/multiplication'
DIVISON_SERVICE_URL = os.environ.get('DIVISON_SERVICE_URL') or 'http://localhost:3002/division'
SUBSTRACTION_SERVICE_URL = os.environ.get('SUBSTRACTION_SERVICE_URL') or 'http://localhost:3003/substraction'

@app.route('/')
def index():
    return 'index'

@app.route('/addition', methods=['POST'])
def addition_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post(ADDITION_SERVICE_URL, req_data).json()


@app.route('/multiplication', methods=['POST'])
def multiplication_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post(MULTIPLICATION_SERVICE_URL, req_data).json()


@app.route('/division', methods=['POST'])
def division_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post(DIVISON_SERVICE_URL, json.dumps(req_data)).json()


@app.route('/substraction', methods=['POST'])
def substraction_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post(SUBSTRACTION_SERVICE_URL, req_data).json()


def generate_req_data(number1, number2):
    return {
        "number1": number1,
        "number2": number2
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
