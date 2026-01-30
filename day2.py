#TIP CALCULATOR

print("Welcome to the tip calculator!")
totalBill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
totalPerson=int(input("How many people to split the bill?"))
print(f"Each person should pay: ${round((totalBill/totalPerson)*(1+tip/100),2)}")