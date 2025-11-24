import math
def add(*args):
    sum = 0
    for n in args:
        sum = sum+n

    print(sum)

add(2,3,10,70)

def calculate(n, **kwargs):
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n)

calculate(2, add=5, multiply=6)