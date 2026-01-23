# Student Management System using Lists


# Create initial list of students
students = ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"]
print("Initial students:", students)


# Add students
students.append("Hassan")          # Add at end
print("After append:", students)


students.insert(2, "Zain")         # Add at index 2
print("After insert:", students)



# Remove students
students.remove("Sara")            # Remove by value
print("After remove:", students)


removed = students.pop()            # Remove last item
print("After pop:", students)
print("Removed student:", removed)


# Slice first 3 students
first_three = students[:3]
print("First 3 students:", first_three)


# Sort list alphabetically
students.sort()
print("Sorted students:", students)
