import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    else:
        logging.info(f'CPU usage is normal: {cpu_usage}%')

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')
    else:
        logging.info(f'Memory usage is normal: {memory_usage}%')

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {disk_usage}% used')
    else:
        logging.info(f'Disk space usage is normal: {disk_usage}% used')

def check_processes():
    processes = psutil.pids()
    logging.info(f'Number of running processes: {len(processes)}')

def monitor_system():
    logging.info('Starting system health check')
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    logging.info('System health check completed')

if __name__ == "__main__":
    monitor_system()
