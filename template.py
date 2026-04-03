import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_folder = "CosmeticDetection"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_folder}/__init__.py",
    f"{project_folder}/components/__init__.py",
    f"{project_folder}/components/data_ingestion.py",
    f"{project_folder}/components/data_validation.py",
    f"{project_folder}/components/model_trainer.py",
    f"{project_folder}/constant/__init__.py",
    f"{project_folder}/constant/training_pipeline/__init__.py",
    f"{project_folder}/constant/application.py",
    f"{project_folder}/entity/config_entitiy.py",
    f"{project_folder}/entity/artifacts_entity.py",
    f"{project_folder}/exception/__init__.py",
    f"{project_folder}/logger/__init__.py",
    f"{project_folder}/pipeline/__init__.py",
    f"{project_folder}/pipeline/training_pipeline.py",
    f"{project_folder}/utils/__init__.py",
    f"{project_folder}/utils/main_utils.py",
    f"{project_folder}/templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directories {filedir} for the file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file:{filename}")
    else:
        logging.info(f"{filename} is already created")