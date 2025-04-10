from flask import Flask,render_template, request
import requests

BACKEND_URL = "http://localhost:9000"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + "/submit", json=form_data)
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)