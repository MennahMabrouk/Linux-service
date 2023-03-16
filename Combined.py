"""
This code is a Python script that collects various metrics related to a computer's workload, 
saves them to a text file, and sends the file via email to a specified recipient every 12 hours.
"""
import psutil  # import psutil module for system information
import time  # import time module for waiting
import os  # import os module for file handling
import smtplib  # import smtplib module for sending emails
from email.mime.text import MIMEText  # import necessary email modules
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def collect_workload():
    # Collect various metrics related to the computer's workload
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_stats = psutil.net_io_counters()
    sent_bytes = network_stats.bytes_sent
    recv_bytes = network_stats.bytes_recv
    
    # Return the metrics in a formatted string
    return 'CPU usage: {}%\nMemory usage: {}%\nDisk usage: {}%\nBytes sent: {}\nBytes received: {}'.format(cpu_percent, memory_percent, disk_percent, sent_bytes, recv_bytes)

def send_email():
    # Define sender and recipient email addresses, and password
    sender_email = '2min0min19@gmail.com'
    receiver_email = 'mennahsameh20@gmail.com'
    password = 'Put your own password'

    # Create a multipart message object
    msg = MIMEMultipart()
    msg['Subject'] = 'PC workload report'  # Set the email subject
    msg['From'] = sender_email  # Set the sender email
    msg['To'] = receiver_email  # Set the recipient email

    # Attach the latest workload text file to the email
    with open('workload.txt', 'r') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('Content-Disposition', 'attachment', filename='workload.txt')
        msg.attach(attachment)

    # Set up the email server and send the email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    smtp.quit()

while True:
    # Open the workload text file, write the latest metrics, and close the file
    with open(os.path.join(os.path.dirname(__file__), 'workload.txt'), 'a') as f:
        f.write(f'{collect_workload()}\n')
    
    time.sleep(60*60*12)  # Wait for 12 hours (in seconds)

    send_email()  # Send the latest workload text file via email
