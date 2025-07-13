import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://flask_user:Bigfix123!@cluster0.iee48.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = "test"
    USER_COLLECTION = "user_details"