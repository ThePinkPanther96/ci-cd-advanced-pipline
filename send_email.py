import os
import smtplib
from email.mime.text import MIMEText

subject = "Advanced pipelibe"
body = "Tests completed successfully"
sender = os.environ.get('SENDER_EMAIL')    
recipients = "gal8156@gmail.com"  
password = os.environ.get('RECIPIENT_PASWD')  

def send_email(subject, body, sender, recipients, password):
    if not sender or not password:
        print("Environment variables for RECIPIENT or SENDER are not set.")
        return

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)