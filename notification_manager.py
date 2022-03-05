from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
my_number=os.getenv("PHONE")
twilio_number=os.getenv("TWILIO_PHONE")
mail = os.getenv("CORREO")
password = os.getenv("PASSWORD")

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid,auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_number,
            to=my_number,
        )
        print(message.sid)
    
    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.office365.com:587") as connection:
            connection.starttls()
            connection.login(mail,password)
            for email in emails:
                connection.sendmail(
                    from_addr=mail,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )