import smtplib  # Import the smtplib library for sending emails
from email.mime.text import MIMEText  # Import the MIMEText class to create the message body
from email.mime.multipart import MIMEMultipart  # Import the MIMEMultipart class to create the email message
from email.mime.application import MIMEApplication  # Import the MIMEApplication class to attach a file to the email

def send_email():
    sender_email = '2min0min19@gmail.com'  # Define the sender email address
    receiver_email = 'mennahsameh20@gmail.com'  # Define the recipient email address
    password = 'put your password here'  # Define the email account password (ideally, this would be stored in a more secure manner)

    msg = MIMEMultipart()  # Create a new message object of type MIMEMultipart
    msg['Subject'] = 'PC workload report'  # Set the email subject line
    msg['From'] = sender_email  # Set the email sender
    msg['To'] = receiver_email  # Set the email recipient

    with open('workload.txt', 'r') as f:  # Open the workload.txt file in read mode
        attachment = MIMEApplication(f.read(), _subtype='txt')  # Create an attachment object of type MIMEApplication, containing the contents of the file
        attachment.add_header('Content-Disposition', 'attachment', filename='workload.txt')  # Add a header to the attachment indicating that it should be treated as an attachment and giving it a filename
        msg.attach(attachment)  # Attach the file to the email message

    smtp_server = 'smtp.gmail.com'  # Set the SMTP server address (in this case, the Gmail server)
    smtp_port = 587  # Set the SMTP server port (587 is the default for Gmail's SMTP server)
    smtp = smtplib.SMTP(smtp_server, smtp_port)  # Create a new SMTP object with the specified server address and port
    smtp.ehlo()  # Identify the client to the server using the EHLO command
    smtp.starttls()  # Start a TLS encrypted session
    smtp.login(sender_email, password)  # Log in to the email account using the provided email address and password
    smtp.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email message
    smtp.quit()  # Quit the SMTP connection

