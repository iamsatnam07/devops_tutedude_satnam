from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus("qwerty@123")
MONGO_URI = f"mongodb+srv://new_user07:{password}@cluster0.iee48.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(MONGO_URI)

db = client.users
collection = db['user_data'] 

app = Flask(__name__)

@app.route("/submit", methods=['POST'])
def submit():
    try:
        form_data = dict(request.form)
        result = collection.insert_one(form_data)
        return "Data submitted succesfully"
    except Exception as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == '__main__':
    app.run(debug=True)