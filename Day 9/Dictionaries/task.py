programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "I have updated the dictionary"

print(programming_dictionary)

empty_dictionary = {}

# empty a dictionary
programming_dictionary = {}

programming_dictionary["Bug"]="This is a bug"

print(programming_dictionary)
# update if Bug is present else inserts the key-value pair
programming_dictionary["Bug"]= "This is updated"
print(programming_dictionary)

# loop through dictionary
for thing in programming_dictionary:
    print(thing) #prints key
    print(programming_dictionary[thing]) #prints the value of the key