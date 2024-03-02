import math

"""
This program is designed to allow the user to chose, and access two different financial calculators:
An investment calculator or a home loan repayment calculator.

In base of in information input by a user:

The program should output the appropriate amount that the user will get back after the given period, 
at the specified interest rate in the case of investment.

The program should calculate and output how much money the user will have to repay each month in the case of bond.

"""
print("FINANCIAL CALCULATION")
print("")

print("investment - to calculate the amount you'll earn on your investment.")
print("bond       - to calculate the amount you'll have to pay on a home loan.")

calculation_chosen = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
print(calculation_chosen)

if calculation_chosen.lower() == "investment":
    money_depositing = float(input("Please, enter the amount you are depositing (in pound): "))
    print(str(money_depositing) + " £")
    p = money_depositing
    
    interest_rate = float(input("Please, enter the interest rate (as percentage): "))
    print(str(interest_rate) + " %")
    r = interest_rate / 100
    
    number_years_investing = float(input("Please, enter the number of years investing: "))
    print(str(number_years_investing) + " Years")
    t = number_years_investing
    
    interest = input("Please, enter the type of interest you want, 'Simple' or 'Compound': ")
    print(interest)

    if interest.lower() == "simple":
        total_amount_simple = p * (1 + r*t)
        a = str(total_amount_simple)
        print("The total amount you'll earn is " + a + " £")

    elif interest.lower() == "compound":
        total_amount_compound = p * math.pow((1 + r), t)
        b = str(total_amount_compound)
        print("The total amount you'll earn is " + b + " £")
    else:
        print("Error message: Please, start over and enter a valid input to proceed")


elif calculation_chosen.lower() == "bond":
    value_house = float(input("Please, enter the present value of the house (in pound): "))
    print(str(value_house) + " £")
    pv = value_house

    annual_interest_rate = float(input("Please, enter the annual interest rate (as percentage): "))
    print(str(annual_interest_rate) + " %")
    monthly_interest_rate = annual_interest_rate / 12
    i = monthly_interest_rate / 100

    number_months_repayment = input("Please, enter the number of months over which the bond will be repaid: ")
    print(number_months_repayment + " months")
    n = float(number_months_repayment)

    repayment = (i * pv) / (1 - (1 +i) ** (-n))
    

    print("The amount you'll have to repay each month is: " + str(repayment) + " £")
    
else:
    print("Error Message: Please, start over and enter a valid input to proceed")
