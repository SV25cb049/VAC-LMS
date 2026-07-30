
from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['lms_db']
courses_collection = db['courses']
submissions_collection = db['submissions']

@app.route('/')
@app.route('/courses')
def courses():
    # Fetch all courses from MongoDB
    all_courses = list(courses_collection.find())
    return render_template('courses.html', courses=all_courses)

@app.route('/course/<course_code>')
def course_detail(course_code):
    
    course = courses_collection.find_one({'code': course_code})
    if not course:
        return "Course not found", 404
    return render_template('course_detail.html', course=course)
@app.route('/submit-assignment', methods=['POST'])
def submit_assignment():
    # Extracting data sent from the HTML form
    course_code = request.form.get('course_code')
    student_name = request.form.get('student_name')
    submission_text = request.form.get('submission_text')

    submission_data = {
        'course_code': course_code,
        'student_name': student_name,
        'submission_text': submission_text
    }
    submissions_collection.insert_one(submission_data)
    course = courses_collection.find_one({'code': course_code})
    return render_template('course_detail.html', course=course, message="Assignment submitted successfully!")

if __name__ == '__main__':
    app.run(debug=True)