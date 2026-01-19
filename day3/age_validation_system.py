
name = input("Enter your name: ")


try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    elif age < 13:
        print(f"Hello {name}! As a child, enjoy learning and playing.")
    elif age <= 17:
        print(f"Hello {name}! As a teenager, you have many opportunities ahead.")
    elif age <= 64:
        print(f"Hello {name}! As an adult, keep growing and achieving.")
    else:
        print(f"Hello {name}! As a senior, your experience is valuable.")


except ValueError:
    print("Invalid input. Please enter a numeric age.")
