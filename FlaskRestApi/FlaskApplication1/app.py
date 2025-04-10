from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/api")
def jsondata():
    with open('data.json', 'r') as f:
        data = json.load(f)  
        
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000',debug=True)