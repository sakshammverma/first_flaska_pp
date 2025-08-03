from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sem', methods=['POST'])
def sem_post_redirect():
    sem_id = request.form['sem_id']
    return redirect(f'/sem/{sem_id}')
 
semesters = {
    "sem1": [
        ("Mathematics-I", 4),
        ("Programming for Problem Solving", 4),
        ("Chemistry", 4),
        ("Soft Skill", 2),
        ("Engineering Graphics", 3),
        ("Workshop", 1.5),
        ("Chemistry Lab", 1),
        ("Programming Lab", 1.5)
    ],
    "sem2": [
        ("Mathematics-II", 4),
        ("Physics", 4),
        ("Basic Electrical Engineering", 4),
        ("Electronics Engineering", 3),
        ("Engineering Mechanics", 3),
        ("Physics Lab", 1),
        ("Electrical Lab", 1),
        ("Electronics Lab", 1),
        ("Engineering Mechanics Lab", 1)
    ],
    "sem3": [
        ("Discrete Structures & Theory of Logic", 3),
        ("Computer Organization and Architecture", 3),
        ("Data Structures", 4),
        ("Software Engineering", 3),
        ("Constitution of India, Law and Engineering", 1),
        ("Data Structures Lab", 1),
        ("Computer Organization Lab", 1),
        ("Mini Project", 2)
    ],
    "sem4": [
        ("Operating Systems", 4),
        ("Theory of Automata and Formal Languages", 3),

        ("Cyber security", 2),
        ("Universal Human Values", 2),
        ("Operating Systems Lab", 1),
        ("DBMS Lab", 1),
        ("Microprocessor Lab", 1),
        ("Mini Project", 2)
    ],
    "sem5": [
        ("Design and Analysis of Algorithms", 4),
        ("Compiler Design", 3),
        ("Computer Networks", 3),
        ("Industrial Management", 2),
        ("Open Elective-I", 3),
        ("DAA Lab", 1),
        ("CN Lab", 1),
        ("Compiler Design Lab", 1),
        ("Mini Project", 2)
    ],
    "sem6": [
        ("Artificial Intelligence", 4),
        ("Web Technology", 3),
        ("Open Elective-II", 3),
        ("Departmental Elective-I", 3),
        ("Project", 3),
        ("AI Lab", 1),
        ("Web Tech Lab", 1),
        ("Seminar", 1)
    ],
    "sem7": [
        ("Machine Learning", 3),
        ("Big Data", 3),
        ("Departmental Elective-II", 3),
        ("Open Elective-III", 3),
        ("Project Phase-I", 4),
        ("Machine Learning Lab", 1),
        ("Big Data Lab", 1)
    ],
    "sem8": [
        ("Cloud Computing", 3),
        ("Cyber Security", 3),
        ("Departmental Elective-III", 3),
        ("Project Phase-II", 6),
        ("Internship/Training", 4)
    ]
}


@app.route('/sem/<sem_id>')
def sem_page(sem_id):
    subjects = semesters.get(sem_id, [])
    return render_template("sem_select.html", sem_id=sem_id, subjects=subjects)

@app.route('/calculate/<sem_id>', methods=["POST"])
def calculate(sem_id):
    subjects = semesters.get(sem_id, [])
    total_credits = sum(cr for (_, cr) in subjects)
    total_weighted = 0

    for i, (subject, credit) in enumerate(subjects):
        internal = float(request.form.get(f"internal_{i}"))
        external = float(request.form.get(f"external_{i}"))
        total_marks = internal + external  

        grade = (total_marks / 100) * 10
        total_weighted += credit * grade


    sgpa = round(total_weighted / total_credits, 2)

    return f"<h2>Your SGPA for {sem_id} is: {sgpa}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
