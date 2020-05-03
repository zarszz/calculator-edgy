from flask import Flask, request, Response
from math import floor

import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'index'

@app.route('/division', methods=['POST'])
def division():
    req_data = request.get_json(force=True)
    result = floor(int(req_data['number1']) / int(req_data['number2']))
    data = {
        "status": "success",
        "result": result,
    }
    return Response(response=json.dumps(data), status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(port=3002, debug=True)