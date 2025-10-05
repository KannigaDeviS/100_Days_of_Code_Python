# Range function
# range is used for iterations
for number in range(1,10):
    print(number)
print("******************************")
for number in range(1,11,3):
    print(number)
print("******************************")
# print 5, 10, 15,....100
for number in range(5,100,5):
    print(number)


print("******************************")
# total of numbers between 1 and 100 inclusive of both 1 and 100
sumOf100 = 0
for number in range(1,101):
    sumOf100 += number

print(sumOf100)
