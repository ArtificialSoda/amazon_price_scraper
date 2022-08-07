import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('TEST_EMAIL')
EMAIL_PASSWORD = os.environ.get('TEST_PASSWORD')

msg = EmailMessage()

msg['Subject'] = 'Hi!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'xynnax6@gmail.com'
msg.set_content("How are you?")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

    print("SUCCESS!")




