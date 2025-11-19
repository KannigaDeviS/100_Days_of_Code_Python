# with open('weather_data.csv') as weather_data_from_csv:
#     weather_data = weather_data_from_csv.readlines()

# import csv
# with open('weather_data.csv') as weather_data_from_csv:
#     weather_data = csv.reader(weather_data_from_csv)
#     temperatures = []
#     for weather in weather_data:
#         if weather[1].isdigit():
#             temperatures.append(int(weather[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data)) #dataframe
# print(data)
# print(type(data["temp"])) # series
# print(data["temp"]) #temp is the column name
#
# data_dict = data.to_dict()
# print(data_dict) #converts datastream to dictionary
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# challenge1: calculate average of temperatures
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)

#using build in function
# import numpy as np
# print(np.average(temp_avg))

# using pandas
# print(data["temp"].mean())

# challenge2: get maximum number from the list
# print(data["temp"].max())


# Get data in column
# print(data["temp"])
# print(data.temp)

# Get data in row
# print(data[data.day == 'Monday'])

# Get the data row that has the highest temperature
# print(data[data.temp == data.temp.max()])

# Get the data row that has the highest temperature and access one of its column
# print(data[data.temp == data.temp.max()].condition)

# Challenge: get the monday's temperature in fahrenheit
# print((data[data.day=='Monday'].temp * 1.8)+32)


# creating a dataframe
# import pandas
# data_dict = {
#     "students":["Kanniga", "Kaushik", "Reeyan"],
#     "score":[20,30,40]
# }
# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
#convert dataframe to csv
# data_frame.to_csv('data_frame.csv')

# challenge: extract the column primary Fur colour and count no of squirrels with each fur color
import pandas
census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(primary_fur_color_data)
counts_df = census_data['Primary Fur Color'].value_counts().reset_index()
counts_df.columns = ['Fur Colour', 'Count']
counts_df.to_csv('squirrel_count.csv')