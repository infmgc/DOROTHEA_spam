import smtplib
import time
host="smtp-mail.outlook.com"
sender = 'hola.soy.tu.bot@outlook.es'
receivers = ['nasivir198@gyxmz.com']
message = """From: From Person <hola.soy.tu.bot@outlook.es>
To: To Person <nasivir198@gyxmz.com>
Subject: SMTP email example


This is a test message.
"""       
mails=5  
while mails > 0:
    try:     
        print("envio correo")
        smtpObj = smtplib.SMTP(host, 587) 
    except Exception as e :
        print (e) 
        smtpObj = smtplib.SMTP_SSL(host, 465)
        
    smtpObj.ehlo() 
    smtpObj.starttls()
    smtpObj.login('hola.soy.tu.bot@outlook.es', "12Sr2%!psZcI")
    smtpObj.sendmail(sender, receivers, message)
    print("enviado correctamente")
    time.sleep(5)
    mails = mails - 1
