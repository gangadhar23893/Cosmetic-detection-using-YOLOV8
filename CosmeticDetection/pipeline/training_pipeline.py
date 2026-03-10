import os
import sys
from CosmeticDetection.logger import logging
from CosmeticDetection.exception import AppException
from CosmeticDetection.components.data_ingestion import DataIngestion
from CosmeticDetection.entity.config_entity import DataIngestionConfig
from CosmeticDetection.entity.artifacts_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("entered data ingestion method of training pipeline")
            logging.info("getting data from url")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info("Exited the start data ingestion method of training pipeline")
            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e,sys)
        
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception  as e:
            raise AppException(e,sys)
        
        