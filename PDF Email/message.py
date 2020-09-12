from email.message import EmailMessage
import mimetypes
import os.path
import smtplib
import getpass

sender = "andresxd1215@gmail.com"
recipient = "varela0311@hotmail.com"
mail_pass = getpass.getpass('Password? ')
message = "hello"
message = EmailMessage()
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = """Hey there! I'm learning to send emails using Python!"""
message.set_content(body)


attachment_path = "CCITT_1.TIF"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),maintype=mime_type,subtype=mime_subtype,filename=os.path.basename(attachment_path))

server = smtplib.SMTP_SSL('smtp.gmail.com')
server.login(sender, mail_pass)
print("Logins sucess")
server.send_message(message)
print("Email has ben sent to {}".format(recipient))
server.quit()

