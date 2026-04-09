import os
import sys
import yaml
import shutil
import zipfile
from ultralytics import YOLO
from CosmeticDetection.utils.main_utils import read_yaml_file
from CosmeticDetection.logger import logging
from CosmeticDetection.exception import AppException
from CosmeticDetection.entity.config_entitiy import ModelTrainerConfig
from CosmeticDetection.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config
    
    def initiate_model_trainer(self)->ModelTrainerArtifact:
        logging.info('Entered initiate model trainer method of model trainer class')
        try:
            logging.info("Unzipping the data")
            os.system("unzip data.zip")
            os.system("rm data.zip")

            temp_dir  = "temp_trainig"
            exp_name = "yolo_exp"

            model_trainer_dir = os.makedirs(self.model_trainer_config.model_trainer_dir,exist_ok=True)
            
            logging.info(f"Loading YOLOV8N model")
            model = YOLO(self.model_trainer_config.weight_name)

            logging.info(f"Starting model training")
            model.train(
                data = "./data.yaml",
                epochs = self.model_trainer_config.no_epochs,
                imgsz=640,
                batch=self.model_trainer_config.batch_size,
                workers=0,
                device="cpu",
                project = temp_dir,
                name=exp_name,
                plots=True,
                cache=False,
                amp=False
            )

            best_model_src = os.path.join(
                temp_dir,
                exp_name,
                "weights",
                "best.pt"
            )

            best_model_dest = os.path.join(
                model_trainer_dir,
                "best.pt"
            )

            shutil.copy(best_model_src, best_model_dest)

            logging.info(f"Best model copied to: {best_model_dest}")

            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
                logging.info("Temporary training folder removed")

            shutil.rmtree("./runs")
            shutil.rmtree("./train")
            shutil.rmtree("./valid")
            os.remove("./data.yaml")
            

            return ModelTrainerArtifact(
                trained_model_file_path=best_model_dest
            )
            
        except Exception as e:
            raise AppException(e,sys)
        