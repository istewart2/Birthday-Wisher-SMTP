import smtplib

my_email = "EMAIL GOES HERE"
password = "PASSWORD GOES HERE"
receiver_email = "RECEIVER EMAIL GOES HERE"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiver_email,
                        msg="Subject:Hello\n\nThis is the email body.")
