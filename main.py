import csv

from sendemail import sendemail

sender_name = input("Sender name: ").strip().capitalize()
sender_email = input("Sender email: ").strip().lower()
subject = input("Subject: ").strip()
body = ""

with open("body-template.txt", "r") as file:
    body_template = file.read()

with open("recipients-list.csv", "r") as file:
    csv_dict = csv.DictReader(file)
    for line_data in csv_dict:
        recipient_email = line_data["email"]
        body = body_template

        body = body.replace("%UNIVERSITY%", line_data["university"])
        body = body.replace("%RECIPIENT%", line_data["recipient"])
        body = body.replace("%NAME%", sender_name)

        sendemail(sender_email, recipient_email, subject, body)

print("\nMessages sent.")
