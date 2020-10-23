import requests_debugger
import requests
import smtplib 
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
s = smtplib.SMTP('smtp.gmail.com', 587) 
username=os.environ.get("Username")
password=os.environ.get("Password")
print(username)
print(password)
mail_content = '''Hello,
    There is slight variation in your infra only mode hosts
    '''

sender_address = username
sender_pass = password
receiver_address = 'deepakprakash205@gmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Alert'   
message.attach(MIMEText(mail_content, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587) 

session.starttls() 
session.login(sender_address, sender_pass)

text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()

