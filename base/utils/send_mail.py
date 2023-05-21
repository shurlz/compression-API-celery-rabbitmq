import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()


def send_email(to, subject, message):

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = os.environ.get('EMAIL_ADDRESS')
    msg['To'] = to
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ.get('EMAIL_ADDRESS'), os.environ.get('EMAIL_PASSWORD'))
        smtp.send_message(msg)
