# Grade Tracker using Parallel Lists

student_names = ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"]
student_grades = [78, 45, 88, 66, 52]


# Highest grade
highest_grade = max(student_grades)
highest_index = student_grades.index(highest_grade)
print("Highest Grade:", student_names[highest_index], "-", highest_grade)


# Lowest grade
lowest_grade = min(student_grades)
lowest_index = student_grades.index(lowest_grade)
print("Lowest Grade:", student_names[lowest_index], "-", lowest_grade)


# Average grade
average_grade = sum(student_grades) / len(student_grades)
print("Average Grade:", average_grade)


# Passed students
print("Passed Students (>=50):")
for i in range(len(student_grades)):
    if student_grades[i] >= 50:
        print(student_names[i], "-", student_grades[i])
