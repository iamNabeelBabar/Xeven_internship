"""
Purpose: Demonstrate basic Python data types and type conversion
Nabeel Babar

"""

# Integer
age = 22
print("Age:", age, " Type:", type(age))

# Float
pi_value = 3.14
print("Pi:", pi_value, " Type:", type(pi_value))

# Boolean
is_ai_student = True
print("AI Student:", is_ai_student, " Type:", type(is_ai_student))

# String
name = "Nabeel"
print("Name:", name, " Type:", type(name))

# Type conversion
age_str = str(age)
pi_int = int(pi_value)

print("Converted age:", age_str, type(age_str))
print("Converted pi:", pi_int, type(pi_int))
