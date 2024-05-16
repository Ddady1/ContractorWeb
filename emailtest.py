import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server_account = 'XXXX@tadiran-group.co.il' #authorized account
server_password = 'XXXXXXXXXXXXXXX' #password for account

msg = MIMEMultipart()
msg["Subject"] = "Test from Python" # subject of message
msg["From"] = "XXXX@tadiran-group.co.il" #valid user on server
msg["To"] = "XXXXX@gmail.com" #list of recipients if more than one
msg["Cc"] = "" #optional
body = MIMEText("Python ROCKS") #body of message
msg.attach(body)

smtp = smtplib.SMTP('smtp.office365.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login(server_account, server_password)
smtp.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
smtp.quit()