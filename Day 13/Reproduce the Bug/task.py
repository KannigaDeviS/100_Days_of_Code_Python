from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])
''' The list is from 0 to 5 but random integer is generated from 1 to 6 both inclusive
    so, the list goes out of its boundary and hence the error IndexError: list index out of range'''

# Fix is as below

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])