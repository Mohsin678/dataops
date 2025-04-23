import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(Log_path,exist_ok=True)

Log_file_path = os.path.join(Log_path,LOG_FILE)
logging.basicConfig(
    filename=Log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ =="__main__":
    logging.info("logging has started")