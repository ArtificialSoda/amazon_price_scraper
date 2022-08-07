import smtplib
import os

EMAIL_ADDRESS = os.environ.get('TEST_EMAIL')
EMAIL_PASSWORD = os.environ.get('TEST_PASSWORD')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Hi!'
    body = 'How are you?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'xynnax6@gmail.com', msg)
    print("SUCCESS!")




