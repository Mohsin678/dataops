import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logging.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} with file name of {filename}")

    
    if (not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass
            logging.info(f"creating empty file:{filepath}")

    else:
        logging.info(f"{filename}already exists")
            

    








