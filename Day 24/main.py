#file_location = '/Users/kanni/OneDrive/Desktop/my_file.txt' #absolute path
file_location = '../../../OneDrive/Desktop/my_file.txt'
#file_location = 'my_file.txt'

file = open(file_location)
contents = file.read()
print(contents)
file.close() # we need to close the file


with open(file_location, mode = "a") as file1:
    file1.write("\n I love programming")


