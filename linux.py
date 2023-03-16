import psutil
import time
import os

def collect_workload():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_stats = psutil.net_io_counters()
    sent_bytes = network_stats.bytes_sent
    recv_bytes = network_stats.bytes_recv
    
    return 'CPU usage: {}%\nMemory usage: {}%\nDisk usage: {}%\nBytes sent: {}\nBytes received: {}'.format(cpu_percent, memory_percent, disk_percent, sent_bytes, recv_bytes)

while True:
    with open(os.path.join(os.path.dirname(__file__), 'workload.txt'), 'a') as f:
        f.write(f'{collect_workload()}\n')
    time.sleep(60)
