from twilio.rest import Client

TWILIO_SID = 'ACffbfca30085f45ddc0077173c7452325'
TWILIO_AUTH_TOKEN = '10d32b59d61cf46de3158144ec2951c1'
TWILIO_VIRTUAL_NUMBER = '+16305997254'
TWILIO_VERIFIED_NUMBER = '+251716415744'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        import requests


