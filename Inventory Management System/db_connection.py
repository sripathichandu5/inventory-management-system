import pymysql
import pymongo

def connect_mysql():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="987654321",  # Replace with your MySQL password
            database="inventory_db"
        )
        print("Connected to MySQL!")
        return conn
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def connect_mongodb():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print("Connected to MongoDB!")
        return client["inventory_db"]
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
