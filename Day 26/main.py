# List comprehension
# pattern: new_list = [new_item for item in old_list]
numbers=[1,2,3]
number1=[n+1 for n in numbers]
print(number1)
name ="Kanniga"
namenew=[letter for letter in name]
print(namenew)
newranged =[n+n for n in range(1,5)]
print(newranged)

# Conditional comprehension
# pattern: new_list = [new_item for item in old_list if test]
# name_list =["Aaradhya Harinee", "Aarnavi Sashtika", "Reeyan Aariv", "Kimmaya", "Tarniya"]
# short_namelist = [name for name in name_list if len(name)<8]
# print(short_namelist)
# long_namelist = [name.upper() for name in name_list if len(name)>= 8]
# print(long_namelist)


# Dictionary Comprehension
# pattern: new_dict = {newkey:newvalue for item in item_list}
#name_list =["Aaradhya Harinee", "Aarnavi Sashtika", "Reeyan Aariv", "Kimmaya", "Tarniya"]
import random
# student_dict = {student:random.randint(0,100) for student in name_list}
# print(student_dict)
# passed_students = {key:value for (key, value) in student_dict.items() if value>=60}
# print(passed_students)


# Dataframe Iteration
import pandas
students={"names":["Aaradhya Harinee", "Aarnavi Sashtika", "Reeyan Aariv", "Kimmaya", "Tarniya"],
          "score": [52, 94, 100, 46, 21]}

student_dataframe = pandas.DataFrame(students)
print(student_dataframe)

# for (key, value) in student_dataframe.items():
#     print(key)
#     print(value)

for (index, row) in student_dataframe.iterrows():
    if row.names == "Aaradhya Harinee":
        print(row.score)