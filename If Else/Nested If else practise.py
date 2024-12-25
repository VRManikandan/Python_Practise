salery = int(input())
age = int(input())

if (salery>=20000 or age<=25):
    required_loan_amount = int(input())
    if (required_loan_amount<=50000):
        print("you are eligible for loan")
    else:
        print("maximum loan amount is 50000")
else:
    print("you are not eligible for loan")
    
