year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")



# 1994 does not fall under both the if conditions so nothing is printed
# Fix by updating if or elif such that 1994 is included
# Example
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

#or

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")