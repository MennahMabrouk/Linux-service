import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email():
    sender_email = '2min0min19@gmail.com'
    receiver_email = 'mennahsameh20@gmail.com'
    password = 'put your password here'

    msg = MIMEMultipart()
    msg['Subject'] = 'PC workload report'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with open('workload.txt', 'r') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('Content-Disposition', 'attachment', filename='workload.txt')
        msg.attach(attachment)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    smtp.quit()
