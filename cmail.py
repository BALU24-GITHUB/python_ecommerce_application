import smtplib
from smtplib import SMTP 
from email.message import EmailMessage

def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('darrusaibalaji@gmail.com','qfnd wdlt ykbc kbpc')
    msg=EmailMessage()
    msg['From']='darrusaibalaji02@gmail.com'
    msg['subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()