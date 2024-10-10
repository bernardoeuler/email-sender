from email.message import EmailMessage
import os
import smtplib
import dotenv

dotenv.load_dotenv()

GOOGLE_PASSWORD = os.getenv("GOOGLE_PASSWORD")


def sendemail(sender_email, receiver_email, subject, body):
    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(body)

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(sender_email, GOOGLE_PASSWORD)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    print(f"\nEmail sent from {sender_email} to {receiver_email}.")
    smtp.quit()

    return msg.as_string()
