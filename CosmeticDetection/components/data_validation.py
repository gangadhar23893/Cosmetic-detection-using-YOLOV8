import os
import sys
import shutil
from CosmeticDetection.logger import logging
from CosmeticDetection.exception import AppException
from CosmeticDetection.entity.config_entitiy import DataValidationConfig
from CosmeticDetection.entity.artifacts_entity import DataIngestionArtifact,DataValidationArtifact

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
        except Exception as e:
            raise AppException(e,sys)
    
    def validate_all_files_exist(self)->bool:
        try:
            validation_status=True
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            for file in all_files:
                if file not in self.data_validation_config.required_files_list:
                    validation_status=False
                    break
                if file in ["train","valid"]:
                    internal_files = os.listdir(os.path.join(self.data_ingestion_artifact.feature_store_path,file))
                    for sub_file in self.data_validation_config.sub_files_list:
                        if sub_file not in internal_files:
                            validation_status=False
                            break

                if not validation_status:
                    break

            os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
            with open(self.data_validation_config.valid_status_file_DIR,'w') as f:
                f.write(f"validation_status:{validation_status}")
                
            return validation_status
        except Exception as e:
            raise AppException(e,sys)
    def initiate_data_validation(self)->DataValidationArtifact:
        logging.info(f"Entered initiate data validation function of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(validation_status=status)
            logging.info(f"Exited initiate data_validation_method of data validation class")
            logging.info(f"data_validation_artifact:{data_validation_artifact}")
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path,os.getcwd())
            return data_validation_artifact
        except Exception as e:
            raise AppException(e,sys)

