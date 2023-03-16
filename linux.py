# Import necessary modules
import psutil  # For collecting system information
import time    # For waiting between data collection
import os      # For interacting with the file system

# Define a function to collect system information
def collect_workload():
    # Get the percentage of CPU usage
    cpu_percent = psutil.cpu_percent()
    # Get the percentage of virtual memory usage
    memory_percent = psutil.virtual_memory().percent
    # Get the percentage of disk usage for the root partition
    disk_percent = psutil.disk_usage('/').percent
    # Get the network I/O statistics
    network_stats = psutil.net_io_counters()
    # Get the number of bytes sent over the network
    sent_bytes = network_stats.bytes_sent
    # Get the number of bytes received over the network
    recv_bytes = network_stats.bytes_recv
    
    # Return a string with all the collected information formatted
    return 'CPU usage: {}%\nMemory usage: {}%\nDisk usage: {}%\nBytes sent: {}\nBytes received: {}'.format(cpu_percent, memory_percent, disk_percent, sent_bytes, recv_bytes)

# Infinite loop to collect data and write to file
while True:
    # Open the 'workload.txt' file in append mode
    with open(os.path.join(os.path.dirname(__file__), 'workload.txt'), 'a') as f:
        # Write the collected data to the file
        f.write(f'{collect_workload()}\n')
    # Wait for 60 seconds before collecting data again
    time.sleep(60)
