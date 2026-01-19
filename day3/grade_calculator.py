
try:
    marks = float(input("Enter your marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        
    elif marks >= 90:
        print("Grade A: Excellent work!")
        
    elif marks >= 80:
        print("Grade B: Good job!")
        
    elif marks >= 70:
        print("Grade C: Fair effort, keep improving.")
        
    elif marks >= 60:
        print("Grade D: You passed, but need more practice.")
        
    else:
        print("Grade F: Don't give up, try again!")
        
        

except ValueError:
    print("Invalid input. Please enter numeric marks.")
