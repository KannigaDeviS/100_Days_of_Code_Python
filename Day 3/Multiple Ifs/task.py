print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Teen ticket is $7.")
    else:
        bill = 12
        print("Adult ticket is $12.")

    wantPhoto = input("Do you want a photo: Y or N")
    if wantPhoto=='Y':
        bill+=3
        print("Photo costs you additional $3")

    print(f"Final bill amount is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
