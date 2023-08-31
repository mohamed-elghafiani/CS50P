from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from random import randint


code = randint(1000, 9999)

email = "medlee38@gmail.com"
password = "rbeefekhngmenrdp"

message = MIMEMultipart("alternative")

message["From"] = email
message["To"] = email
message["Subject"] = "Confirmation code!"

text = f"""
    Your verification code is:

    {code}

    Best reagrds,
"""

html = f""""
    <strong> Your verification code is: </strong>

    <h2> {code} </h2>

    Best reagrds,
"""

text = MIMEText(text, "plain")
html = MIMEText(html, "html")

message.attach(text)
message.attach(html)

with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as server:
    server.login(email, password)
    server.sendmail(email, email, message.as_string())
    print("Email was sent!")

verify = int(input("verify: "))

if verify == code:
    print("You were successfully verified!")
else:
    print("Oops That's not correct!")
