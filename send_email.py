import smtplib, os

sender = os.getenv("sender")
receiver = os.getenv("receiver")
password = os.getenv("password")

#def send_email():
    #print("Email sent!")