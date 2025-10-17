def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
''' For loop is running from 1 to 19 and printing a message when a condition is met'''
# 2. When is the function meant to print "You got it"?
''' when i is 20 '''
# 3. What are your assumptions about the value of i?
'''I never becomes 20 so the message won't get printed out'''

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")



