marks = float(input("Enter the marks of the student: "))

if marks > 90:
    extracurricular = input(
        "Did the student participate in extra-curricular activities? (yes/no): "
    ).lower()
    if extracurricular == "yes":
        grade = "Grade A+"
    else:
        grade = "Grade A"
elif 60 <= marks <= 90:
    grade = "Grade B"
else:
    grade = "Grade C"

print(f"The student's grade is: {grade}")
