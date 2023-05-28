#!/usr/bin/env python3 

import smtplib
import imaplib
from email.mime.text import MIMEText

def send_email(smtp_server, smtp_port, sender_email, sender_name, 
               sender_password, recipient_email, subject, message):
    # Create a MIME message
    email_message = MIMEText(message)
    email_message['Subject'] = subject
    email_message['From'] = f"{sender_name} <{sender_email}>"
    email_message['To'] = recipient_email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()  # Enable secure connection
        smtp.login(sender_email, sender_password)
        smtp.send_message(email_message)

# Example usage
if __name__ == "__main__":
    smtp_server = "mail.privateemail.com"
    sender_email = "developers@smswithoutborders.com"
    password = ""
    recipient_email=""
    subject = "We reconfigured our IMAP server"
    message = "Hi Sherlock\nWe have reconfigured the IMAP, hope you receive this email this time. Please let us know.\nMany thanks"
    smtp_port = 587
    sender_name=""

    send_email(smtp_server=smtp_server, smtp_port=smtp_port, 
               sender_email=sender_email, sender_password=password, 
               recipient_email=recipient_email, subject=subject, 
               message=message, sender_name=sender_name)

