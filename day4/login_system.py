
def validate_login(username, password, age):
    errors = []

    if len(username) < 5:
        errors.append("Username must be at least 5 characters.")

    if len(password) < 8:
        errors.append("Password must be at least 8 characters.")

    if age < 18:
        errors.append("You must be 18 or older to register.")


    if errors:
        print("Access Denied:")
        for err in errors:
            print("- " + err)
        return False
    else:
        print("Access Granted! Welcome,", username)
        return True


try:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    age_input = int(input("Enter your age: "))  # Convert to int


    validate_login(username_input, password_input, age_input)

except ValueError:
    print("Invalid input: Age must be a number.")
