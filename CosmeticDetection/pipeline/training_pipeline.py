import sys
import os
from CosmeticDetection.logger import logging
from CosmeticDetection.exception import AppException
from CosmeticDetection.components.data_ingestion import DataIngestion
from CosmeticDetection.components.data_validation import DataValidation
from CosmeticDetection.entity.config_entitiy import DataIngestionConfig,DataValidationConfig,ModelTrainerConfig
from CosmeticDetection.entity.artifacts_entity import DataIngestionArtifact,DataValidationArtifact,ModelTrainerArtifact
from CosmeticDetection.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info(f"Entered the start data ingestion method of trainpipeline class")
            logging.info(f"getting data from url")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Got the data from URL")
            logging.info(f"Exited the start_data_ingestion methos of TrainingPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        logging.info("Entered Data validation method of trainingpipeline class")
        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"performed data validation operation")
            logging.info(f"Exited the start data validation method of training pipeline")

            return data_validation_artifact
        except Exception  as e:
            raise AppException(e,sys)
        
    def start_model_training(self)->ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise AppException(e,sys)


        
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact= self.start_data_ingestion()

            data_validation_artifact = self.start_data_validation(data_ingestion_artifact= data_ingestion_artifact)
            if data_validation_artifact.validation_status==True:
                model_trainer_artifact = self.start_model_training()
        except Exception as e:
            raise AppException(e,sys)
        