def loan_approval(age, income, credit_score):
    print("Decision Path:")

    if age < 18:
        print("Age < 18 → Reject")
        return "Loan Rejected"

    print("Age >= 18 → Continue")

    if income < 30000:
        print("Income < 30000 → Reject")
        return "Loan Rejected"

    print("Income >= 30000 → Continue")

    if credit_score < 600:
        print("Credit Score < 600 → Reject")
        return "Loan Rejected"

    print("Credit Score >= 600 → Approve")
    return "Loan Approved"


result = loan_approval(age=25, income=50000, credit_score=700)
print("\nFinal Decision:", result)
