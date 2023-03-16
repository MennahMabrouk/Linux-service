
import psutil
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def collect_workload():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_stats = psutil.net_io_counters()
    sent_bytes = network_stats.bytes_sent
    recv_bytes = network_stats.bytes_recv
    
    return 'CPU usage: {}%\nMemory usage: {}%\nDisk usage: {}%\nBytes sent: {}\nBytes received: {}'.format(cpu_percent, memory_percent, disk_percent, sent_bytes, recv_bytes)

def send_email():
    sender_email = '2min0min19@gmail.com'
    receiver_email = 'mennahsameh20@gmail.com'
    password = 'Put your own password'

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

while True:
    with open(os.path.join(os.path.dirname(__file__), 'workload.txt'), 'a') as f:
        f.write(f'{collect_workload()}\n')
    time.sleep(60*60*12) # 12 hours

    send_email()
