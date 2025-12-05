import datetime as dt
import smtplib
import random

day_of_week = dt.datetime.now().weekday()
my_email = "aginnak@gmail.com"
password = "haya xahf nxes gjnk"

# if friday send email
if day_of_week == 4:
    with open('quotes.txt', 'r') as file:
        quotes = [line.strip() for line in file if line.strip()]
        chosen_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(
            from_addr=my_email
            , to_addrs='kannigakaushik@outlook.com'
            , msg=f'Subject:Today'f's motivation\n\n{chosen_quote}')
