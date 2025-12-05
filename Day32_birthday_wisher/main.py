##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import os
import smtplib

folder_path = "./letter_templates"
my_email = "aginnak@gmail.com"
password = ""

letter_templates = [f'./letter_templates/{f}' for f in os.listdir(folder_path) if f.endswith(".txt")]

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_day = today.day
today_month = today.month
today_year = today.year

data = pandas.read_csv('birthdays.csv')
data_dictionary = data.to_dict(orient="records")

for data in data_dictionary:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

    if data['year'] == today_year and data['month'] == today_month and data['day'] == today_day:
        chosen_letter_template = random.choice(letter_templates)
        with open(file = chosen_letter_template,mode= 'r') as l:
            letter = l.read()
            letter = letter.replace("[NAME]", data['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password= password)
            connection.sendmail(
                from_addr=my_email
                , to_addrs=data['email']
                , msg=f'Subject:Happy Birthday!\n\n {letter}')
