import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
# TODO: Write out the other 3 functions - subtract, multiply and divide.
def sub(n1, n2):
    return  n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
print(operations["*"](4,8))
canContinue = True
num1 = 0
num2 = 0
operator = 0
result = 0
while canContinue:
    if num1 == 0:
        num1 = int(input("Input the first number: "))
    operator = input("Type a mathematical operator: ")
    num2 = int(input("Input the second number: "))
    result = operations[operator](num1,num2)
    print(f"The result is {result}")
    choice = input("Do you want to continue working with the previous result? yes or no: ")
    if choice == "no":
        result = 0
        num1 = 0
    else:
        num1 = result
