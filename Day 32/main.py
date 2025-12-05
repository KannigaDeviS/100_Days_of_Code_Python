# import smtplib
#
# my_email = "aginnak@gmail.com"
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password= password)
#     connection.sendmail(
#         from_addr=my_email
#         , to_addrs='kannigakaushik@outlook.com'
#         , msg='Subject:New message\n\n hello! this is test')


import datetime as dt

NOW = dt.datetime.now()
year = NOW.year
month = NOW.month
second = NOW.second
day_of_week = NOW.weekday()
print(day_of_week)


date_of_birth = dt.datetime(year=1996, month=10, day=29, hour=14, minute=1, second=0)
print(date_of_birth)