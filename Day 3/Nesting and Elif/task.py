print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

# without elif
if height >= 120:
    print("You can ride the rollercoaster")
    if age > 18 :
        print("Your ticket cost in $12")
    else:
        if age < 12:
            print("Your ticket cost is $5")
        else :
            print("Your ticket cost is $7")
else:
    print("Sorry you have to grow taller before you can ride.")

# using elif
if height >= 120:
    print("You can ride the rollercoaster")
    if age > 18 :
        print("Your ticket cost in $12")
    elif age < 12:
        print("Your ticket cost is $5")
    else :
        print("Your ticket cost is $7")
else:
    print("Sorry you have to grow taller before you can ride.")
