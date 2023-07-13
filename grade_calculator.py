import cgi

# Get the grades from the HTML form
form = cgi.FieldStorage()
exam_grade = float(form.getvalue("examGrade")) if form.getvalue("examGrade") is not None else 0.0
lab_grade = float(form.getvalue("labGrade")) if form.getvalue("labGrade") is not None else 0.0
quiz_grade = float(form.getvalue("quizGrade")) if form.getvalue("quizGrade") is not None else 0.0

# Perform grade calculation
final_grade = (exam_grade * 0.6) + (lab_grade * 0.2) + (quiz_grade * 0.2)

# Print the result as an HTTP response
print("Content-type: text/html")
print()
print("Final Grade: {:.2f}".format(final_grade))
