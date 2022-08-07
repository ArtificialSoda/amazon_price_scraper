import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('TEST_EMAIL')
EMAIL_PASSWORD = os.environ.get('TEST_PASSWORD')

msg = EmailMessage()

msg['Subject'] = 'Hi! Check out this new leaked GTA6 cover!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'xynnax6@gmail.com'
msg.set_content('See image attached... Crazy, right?')

with open('assets/gta6-cover.jpg', 'rb') as f:
    file_data = f.read()
    file_name = f.name
    file_type = imghdr.what(file_name)
    print(file_type)

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

    print("SUCCESS!")




