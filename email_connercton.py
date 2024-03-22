import smtplib

class SendEmail:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password

    def send_email(self, message: str, email: str):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(self.sender, self.password)
            connection.sendmail(from_addr=self.sender, to_addrs=email,
                                msg=message)

