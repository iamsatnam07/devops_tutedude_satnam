from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import datetime
from config import Config
import bcrypt

app = Flask(__name__)

# Allow CORS for all routes (or restrict to frontend URL)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],  # Allow frontend
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]
users_collection = db[Config.USER_COLLECTION]

# Your existing routes...
@app.route('/', methods=['GET'])
def get_all_users():
    try:
        users = list(users_collection.find({}, {'password': 0}))
        for user in users:
            user['_id'] = str(user['_id'])
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not all([username, email, password]):
        return jsonify({'message': 'All fields are required'}), 400
    
    if len(password) < 8:
        return jsonify({'message': 'Password must be at least 8 characters'}), 400

    if users_collection.find_one({'email': email}):
        return jsonify({'message': 'Email already registered'}), 400
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    user = {
        'username': username,
        'email': email,
        'password': hashed_password.decode('utf-8'),  
        'created_at': datetime.datetime.utcnow(),
        'updated_at': datetime.datetime.utcnow()
    }
    try:
        result = users_collection.insert_one(user)
        return jsonify({
            'message': 'User registered successfully',
            'user_id': str(result.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({'message': f'Registration failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)