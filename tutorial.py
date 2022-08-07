import smtplib
import os

EMAIL_ADDRESS = os.environ.get('TEST_EMAIL')
EMAIL_PASSWORD = os.environ.get('TEST_PASSWORD')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


