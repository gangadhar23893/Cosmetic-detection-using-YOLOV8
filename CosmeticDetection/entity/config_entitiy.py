import os
from dataclasses import dataclass
from datetime import datetime
from CosmeticDetection.constant.training_pipeline import *

@dataclass

class TrainingPipeLineConfig:
    artifacts_dir:str = ARTIFACTS_DIR

training_pipeline_config:TrainingPipeLineConfig=TrainingPipeLineConfig()


@dataclass

class DataIngestionConfig:
    data_ingestion_dir:str = os.path.join(training_pipeline_config.artifacts_dir,DATA_INGESTION_DIR_NAME)

    feature_store_file_path:str = os.path.join(training_pipeline_config.artifacts_dir,DATA_INGESTION_FEATURE_STORE)

    data_download_url:str = DATA_DOWNLOAD_URL


@dataclass

class DataValidationConfig:
    data_validation_dir:str = os.path.join(training_pipeline_config.artifacts_dir,DATA_VALIDATION_DIR_NAME)
    valid_status_file_DIR = os.path.join(data_validation_dir,DATA_VALIDATION_STATUS_FILE)
    required_files_list = DATA_VALIDATION_ALL_REQUIRED_FILES
    sub_files_list = DATA_VALIDATION_FILES_CONTENTS
