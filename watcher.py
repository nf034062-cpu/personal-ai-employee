import os
import shutil
import time
import logging

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_FOLDER = os.path.join(BASE_DIR, "Inbox")
NEEDS_ACTION_FOLDER = os.path.join(BASE_DIR, "Needs_Action")
LOG_FOLDER = os.path.join(BASE_DIR, "Logs")
LOG_FILE = os.path.join(LOG_FOLDER, "watcher.log")

# Create folders if they don't exist
os.makedirs(INBOX_FOLDER, exist_ok=True)
os.makedirs(NEEDS_ACTION_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def move_new_files():
    try:
        for filename in os.listdir(INBOX_FOLDER):
            src = os.path.join(INBOX_FOLDER, filename)
            dst = os.path.join(NEEDS_ACTION_FOLDER, filename)
            shutil.move(src, dst)
            logging.info(f"Moved: {filename}")
            print(f"Moved: {filename}")
    except Exception as e:
        logging.error(f"Error: {e}")

print("Watcher started!")
while True:
    move_new_files()
    time.sleep(10)