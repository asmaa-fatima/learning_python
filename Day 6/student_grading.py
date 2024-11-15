student_scores = {
    "Thomas": 82,
    "Newt": 78,
    "Lisa": 99,
    "Ron": 74,
    "Jennifer": 62,
}

student_grades = {}

for students in student_scores:
    if student_scores[students] > 90:
        student_grades[students] = "Outstanding"
    elif student_scores[students] > 80:
        student_grades[students] = "Exceeds Expectations"
    elif student_scores[students] > 70:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"

print (student_grades)