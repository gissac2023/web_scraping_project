import os
import smtplib
import ssl


def send_email(message):
    sender = os.getenv("sender")
    receiver = os.getenv("receiver")
    password = os.getenv("password")

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


if __name__ == "__main__":
    send_email("this is a test")
