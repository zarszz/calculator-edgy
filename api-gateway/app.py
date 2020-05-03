from flask import Flask, request, Response

import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/addition', methods=['POST'])
def addition_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post('http://localhost:3000/addition', req_data).json()


@app.route('/multiplication', methods=['POST'])
def multiplication_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post('http://localhost:3001/multiplication', req_data).json()


@app.route('/division', methods=['POST'])
def division_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post('http://localhost:3002/division', json.dumps(req_data)).json()


@app.route('/substraction', methods=['POST'])
def substraction_service():
    data = request.get_json(force=True)
    req_data = generate_req_data(data['number1'], data['number2'])
    return requests.post('http://localhost:3003/substraction', req_data).json()


def generate_req_data(number1, number2):
    return {
        "number1": number1,
        "number2": number2
    }

if __name__ == "__main__":
    app.run(debug=True, port=5000)
