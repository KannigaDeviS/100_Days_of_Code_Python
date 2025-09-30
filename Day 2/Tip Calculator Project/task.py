print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tipPercentage = tip/100
billWithTip= bill * tipPercentage
total_bill = bill + billWithTip
Share= total_bill/people
roundedTo = round(Share,2)

print(f"Each of you would pay ${roundedTo}")
