student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# python is number friendly ie) lot of built-in functions to work with numbers
total_score = sum(student_scores) # sum of the numbers in list
print(total_score)
print("******************************")

maximum_score = max(student_scores) # maximum of the numbers in list
print(maximum_score)

max_manual = 0
for s in student_scores :
    if s > max_manual :
        max_manual = s

print(max_manual)