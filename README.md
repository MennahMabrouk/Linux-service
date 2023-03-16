## Linux-service

This project involves creating a Linux server on Zorin OS to collect data about your PC workload, including CPU usage, memory usage, HDD usage, and network usage. The collected data is then saved into a text file.

To accomplish this, you have created a Python script that runs as a systemd service on the Zorin OS server. The script collects the necessary data about the system workload and writes it to a text file at regular intervals. The interval has been set to 12 hours as per the project requirements.

In addition to collecting and saving the data, the script is also responsible for sending an email with the text file attached. The email is sent every 12 hours, along with the latest workload data.

To ensure that the service is always running, you have created a systemd file for it. The systemd file defines the service and specifies how it should be managed by the system. This includes settings such as the service start-up behavior, logging, and resource allocation.

Overall, this project demonstrates how to use Linux and Python to collect and analyze system workload data. It also showcases how to create a systemd service and use it to automate tasks on a Linux server.

## Steps
Install Zorin OS on your server machine.
Open the terminal and install the necessary packages for sending email and collecting system workload data. You can use the following commands to install these packages:
sql
Copy code
sudo apt-get update
sudo apt-get install python3-pip sysstat mailutils
Write a Python script to collect the system workload data and save it to a text file. You can use the psutil module to collect CPU and memory usage data and the iostat command to collect HDD and network usage data. You can save the data to a text file using the csv module in Python.
Create a systemd service file for the Python script. This file should specify the service start-up behavior, dependencies, and resource allocation. You can use a text editor such as Nano or Vim to create the service file. The service file should be saved in the /etc/systemd/system/ directory with a .service extension.
Start the service using the following command:
php
Copy code
sudo systemctl start <service_name>
Enable the service to start automatically on system boot using the following command:
bash
Copy code
sudo systemctl enable <service_name>
Test the service by checking that the text file with system workload data is being created and updated every 12 hours. You can also check that the email is being sent with the text file attached.
That's it! With these steps, you should have a Linux server on Zorin OS that can send an email with PC workload data every 12 hours.
