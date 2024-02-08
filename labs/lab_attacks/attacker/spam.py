import smtplib
from base64 import encodebytes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


host = "smtp-mail.outlook.com"
sender = 'hola.soy.tu.bot@outlook.es'
receivers = 'hola.soy.tu.bot@outlook.es'
message = MIMEMultipart('alternative')
message['From'] = sender
message['To'] = receivers 
message['Subject'] = 'Good morning'
text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
part1 = MIMEText(text, "plain")
message.attach(part1)

# adjunto
attach_path = 'spam.jpg'
with open(attach_path, 'rb') as attach_file:
    part = MIMEBase('application','octet-stream')
    part.set_payload(encodebytes(attach_file.read()).decode())
    part.add_header('Content-Transfer-Encoding', 'base64')
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % attach_path)
message.attach(part)

mails=10
while mails > 0:
    try:
        smtpObj = smtplib.SMTP(host, 25)
    except Exception as e :
        print (e) 
        smtpObj = smtplib.SMTP_SSL(host, 465)
        
    smtpObj.starttls()
    smtpObj.login('hola.soy.tu.bot@outlook.es', "12Sr2%!psZcI!")
    smtpObj.send_message(message)         
    print("Successfully sent email")
    mails = mails - 1
