import random
import my_module
# generate random integer number
#rand_num = random.randint(1, 10)
#print(rand_num)
#print(my_module.my_favourite_number)
# generate random floating point number
#rand_float = random.random()
#print(rand_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")