
ARTIFACTS_DIR :str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION_VAR_NAME
"""

DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE:str = "feature_store"
DATA_DOWNLOAD_URL:str = "https://drive.google.com/file/d/1DVbUpp3V_YCVlXB_KylsniCE3xbWxSsf/view?usp=sharing"


"""
Data Validation related constant start with DATA_VALIDATION_VAR_NAME
"""

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_STATUS_FILE = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train","valid","data.yaml"]
DATA_VALIDATION_FILES_CONTENTS = ['images','labels']


"""
Model trainer related constant start with MODEL TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHTS_NAME:str = "yolov8n.pt"
MODEL_TRAINER_NO_EPOCHS:int = 10
MODEL_TRAINER_BATCH_SIZE:int=16
