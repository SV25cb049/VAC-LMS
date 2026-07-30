
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017/')

db = client['lms_db']
courses_collection = db['courses']

courses_collection.delete_many({})
sample_courses = [
    {
        "code": "py101",
        "title": "Python Programming Basics",
        "category": "Programming",
        "description": "Master fundamental Python syntax, data types, loops, and conditional statements.",
        "content": "Welcome to Python Basics! Python is an interpreted, high-level language. In this module, we cover variables, data structures (Lists, Dictionaries), control flows (If-Else, Loops), and writing functions.",
        "resource_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    },
    {
        "code": "web201",
        "title": "Web Development with Flask & MongoDB",
        "category": "Web Dev",
        "description": "Build dynamic, database-driven web applications using Python, Flask, and MongoDB.",
        "content": "In this module, you will learn how to set up Flask routes, render HTML templates with Jinja2 variables, connect to local MongoDB collections using PyMongo, and handle HTML form submissions.",
        "resource_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    },
    {
        "code": "db301",
        "title": "Database Fundamentals: NoSQL vs SQL",
        "category": "Database",
        "description": "Understand document-based databases like MongoDB and how data is stored in BSON/JSON formats.",
        "content": "This course covers modern database concepts. Learn how NoSQL databases scale efficiently, how collections and documents replace tables and rows, and how to query MongoDB using PyMongo.",
        "resource_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    }
]

courses_collection.insert_many(sample_courses)
print("✅ Successfully seeded LMS database with sample courses!")