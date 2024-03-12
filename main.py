import smtplib
import datetime as dt
import random


def send_email(body):
    my_email = "EMAIL GOES HERE"
    password = "PASSWORD GOES HERE"
    receiver_email = "RECEIVER EMAIL GOES HERE"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Monday Motivation\n\n{body}")


day_of_week = dt.datetime.now().weekday()
if day_of_week == 0:
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
        send_email(random_quote)
