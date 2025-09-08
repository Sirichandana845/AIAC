class Applicant:
    def __init__(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income  # monthly income in INR

    def is_eligible(self):
        # Example criteria: age between 21 and 60, income >= 25000/month
        if 21 <= self.age <= 60 and self.income >= 25000:
            return True
        return False

    def approval_message(self):
        if self.is_eligible():
            return f"Loan Approved for {self.name} (Age: {self.age}, Income: ₹{self.income}/month)"
        else:
            return f"Loan Not Approved for {self.name} (Age: {self.age}, Income: ₹{self.income}/month)"

def main():
    applicants = [
        Applicant("John", 35, 70000),
        Applicant("Priya", 35, 70000)
    ]
    for applicant in applicants:
        print(applicant.approval_message())

if __name__ == "__main__":
    main()
