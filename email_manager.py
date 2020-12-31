import smtplib

class EmailManager:

    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(sender_email, password)


    def send_email(self, reciever_email : str , message: str):
        print("Sending email to {}".format(reciever_email))
        self.server.sendmail(self.sender_email, reciever_email, message)
        
