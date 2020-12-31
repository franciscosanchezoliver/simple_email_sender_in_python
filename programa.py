import smtplib
from email_manager import EmailManager


sender_email = "xxxx@gmail.com"
password = "xxxxx"
email_manager = EmailManager(sender_email, password)

rec_email = "spuzi@hotmail.es"
message = "hola esto es una prueba"
email_manager.send_email(rec_email, message)


