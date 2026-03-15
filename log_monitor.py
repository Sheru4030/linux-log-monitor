import time
import logging

# Configure logging
logging.basicConfig(
    filename="alerts.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

LOG_FILE = "sample.log"

KEYWORDS = ["ERROR", "WARNING", "Failed"]

def monitor_logs():
    with open(LOG_FILE, "r") as file:
        lines = file.readlines()

        for line in lines:
            for keyword in KEYWORDS:
                if keyword in line:
                    print("ALERT:", line.strip())
                    logging.info(line.strip())   # Save alert to alerts.log

while True:
    monitor_logs()
    time.sleep(5)