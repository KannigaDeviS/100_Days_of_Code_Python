try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a numerical value")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")


''' Error Code:
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")
'''
