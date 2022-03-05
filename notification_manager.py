from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
my_number=os.getenv("PHONE")
twilio_number=os.getenv("TWILIO_PHONE")

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