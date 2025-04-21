import logging
import os
from datetime import datetime

Log_file = f"{datetime.now().strftime("")}.log"
Log_path = os.path.join(os.getcwd(),"logs",Log_file)
os.makedirs(Log_path,exist_ok=True)

Log_file_path = os.path.join(Log_path,Log_file)
logging.basicConfig(
    filename=Log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ =="__main__":
    logging.info("logging has started")