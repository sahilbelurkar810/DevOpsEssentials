age = int(input("Enter your age: "))

if 18 <= age <= 60:
    income = int(input("Enter your monthly income: ₹"))
    if income > 30000:
        eligibility = "Eligible for loan"
    else:
        co_signer = input("Do you have a co-signer? (yes/no): ").lower()
        if co_signer == "yes":
            eligibility = "Eligible for loan"
        else:
            eligibility = "Not eligible for loan"
else:
    eligibility = "Not eligible for loan"

print(eligibility)
