# Email sender
This project started as an automated way to send the same email to numerous universities requesting a fee waiver for the Duolingo English Test, as I and my girlfriend were planning on study abroad and we needed to take an English test to prove our proficiency.

Now, I want to make it a more general solution to this type of problem: send the same email to multiple people. And that's what this project is supposed to do.

## How it works
Since the beginning, this project was meant to be simple and straightforward. So I decided to use as few dependencies as possible.

Currently, the program is only supporting Gmail as the SMTP server, so in order to use it you will need a [Google account](https://support.google.com/mail/answer/56256).

### Dependencies
- python-dotenv
- The rest are all part of Python's standard library

### User data
In order to send the email, the program need some data of the user. It inputs the user in the command line for their name, email, and the subject of the message. Additionally, a **Google app password** is needed to authenticate the app to the Gmail SMTP server. This password goes to the `.env` file in the variable `GOOGLE_PASSWORD`.

These app passwords are a way to sign into your Google account on older apps and services that don’t support modern security standards. They can be generated [here](https://myaccount.google.com/apppasswords) and you must have two-factor authentication active to be able to use it.

### Email message template
The message text is located in a file, named `body-template.txt`. The main program reads the text inside it, and replace the placeholders (words in uppercase surrounded by "%") by the desired words.

### Placeholders and variable data
The placeholders gets replaced by words that live within another file, named `recipients-list.csv`, which is a CSV file with the headers being the variable data that will replace the placeholders.

The variable data headers have the same name as their respective placeholders, with the difference that placeholders are uppercased.

In my case, the headers would be **university, recipient, email**. So the respective placeholders would be **%UNIVERSITY%, %RECIPIENT%, %EMAIL%**

### Email sending
FInally, the way the emails get sent. Well, I decided to use Python's built-in module `smtplib` to do the work. It uses an smtp server to send the emails, then it uses TLS to encrypt the data being sent. This module is built-in and very simple to use, so it was the best choice for me.

After setting up the connection to the SMTP server, the program reads the message body template and read the list of recipients. After that, the program takes the recipients data, replaces the placeholders with it and sends the email to them, doing that for each recipient.