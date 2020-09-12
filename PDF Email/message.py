import email.message 
import mimetypes
import os.path
import smtplib
import getpass


def generate(sender, recipient, subject, body, attachment_path):
    """create basic email with attachment"""
    # Basic Email information
    message = email.massage.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    # Process the attachment and add it to the email

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)
    
    return message

def send(message,sender):
    """Sends_message to the configured SMTP server"""
    mail_pass = getpass.getpass('Password? ')
    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.login(sender, mail_pass)
    print("Logins sucess.")
    server.send_message(message)
    print("Email has ben sent to.")
    server.quit()   

