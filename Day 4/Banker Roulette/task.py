import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# approach 1
random_string = random.choice(friends)
print(random_string) # Output: Randomly selected string

# approach 2
length_of_list = len(friends)
print(friends[random.randint(0,length_of_list)])