from flask import Flask, jsonify
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the API. Use /data to fetch processed data."

@app.route('/data')
def get_data():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)
    # Select only name and email
    result = df[['name', 'email']].to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

