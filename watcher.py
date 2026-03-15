import os
import shutil
import time
import logging

# Configuration
# Define the base directory relative to the script's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_FOLDER = os.path.join(BASE_DIR, "Inbox")
NEEDS_ACTION_FOLDER = os.path.join(BASE_DIR, "Needs_Action")
LOG_FOLDER = os.path.join(BASE_DIR, "Logs")
LOG_FILE = os.path.join(LOG_FOLDER, "watcher.log")

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def move_new_files():
    try:
        # Ensure Inbox folder exists, log if not found
        if not os.path.exists(INBOX_FOLDER):
            logging.warning(f"Inbox folder not found: {INBOX_FOLDER}")
            return

        # Create Needs_Action folder if it doesn't exist
        if not os.path.exists(NEEDS_ACTION_FOLDER):
            os.makedirs(NEEDS_ACTION_FOLDER)
            logging.info(f"Created Needs_Action folder: {NEEDS_ACTION_FOLDER}")

        # Iterate through files in the Inbox folder
        for filename in os.listdir(INBOX_FOLDER):
            file_path = os.path.join(INBOX_FOLDER, filename)

            # Process only files, not directories
            if os.path.isfile(file_path):
                destination_path = os.path.join(NEEDS_ACTION_FOLDER, filename)
                shutil.move(file_path, destination_path)
                logging.info(f"Moved file: {filename} to {NEEDS_ACTION_FOLDER}")

    except Exception as e:
        logging.error(f"An error occurred during file move: {e}")

if __name__ == "__main__":
    # Create necessary directories if they don't exist
    os.makedirs(INBOX_FOLDER, exist_ok=True)
    os.makedirs(NEEDS_ACTION_FOLDER, exist_ok=True)
    os.makedirs(LOG_FOLDER, exist_ok=True)

    logging.info("Watcher script started. Monitoring Inbox folder...")

    try:
        while True:
            move_new_files()
            time.sleep(5) # Check every 5 seconds
    except KeyboardInterrupt:
        logging.info("Watcher script stopped by user.")
        print("Watcher script stopped.")
