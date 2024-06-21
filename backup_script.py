import os
import subprocess
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Configuration
SOURCE_DIRECTORY = '/Users/sauravkumar/Desktop'
REMOTE_SERVER = 'saurav@remote_server:/Users/sauravkumar/Desktop'

def run_backup():
    logging.info('Starting backup operation')
    try:
        result = subprocess.run(['rsync', '-avz', SOURCE_DIRECTORY, REMOTE_SERVER], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info('Backup completed successfully')
        logging.info(f'rsync output: {result.stdout.decode()}')
    except subprocess.CalledProcessError as e:
        logging.error('Backup failed')
        logging.error(f'rsync error output: {e.stderr.decode()}')

if __name__ == "__main__":
    run_backup()
