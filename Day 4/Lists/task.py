fruits = ["Cherry", "Apple", "Pear"]
print(fruits[0]) # lists index starts with 0

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[-1]) # prints last item in list
states_of_america[1] = "Pencilvania" # alter items in the list via index
print(states_of_america)

states_of_america.append("Angeland") #add an item to end of list
print(states_of_america)

states_of_america.extend(["Hey","everyone"]) #add a list of items to end of list
print(states_of_america)

#more list operations
# https://docs.python.org/3/tutorial/datastructures.html