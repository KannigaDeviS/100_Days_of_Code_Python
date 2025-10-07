# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# function with multiple parameter
def greet_with_name(name, location):
    print(f"Hello! {name}")
    print(f"How are you doing? {name}")
    print(f"Are you from {location}?")
# calling with positional argument
greet_with_name("Kanniga","Chennai")

# function with multiple parameter
def greet_with_name(name, location):
    print(f"Hello! {name}")
    print(f"How are you doing? {name}")
    print(f"Are you from {location}?")
# calling with keyword argument
greet_with_name(location="Chennai", name="Kanniga")
