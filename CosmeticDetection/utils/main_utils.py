import os.path
import sys
import yaml
import base64
from CosmeticDetection.exception import AppException
from CosmeticDetection.logger import logging

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,"rb") as yaml_file:
            logging.info("Read yaml file succesful")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys)

def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            with open(file_path,"w") as file:
                yaml.dump(content,file)
                logging.info("succesfully written to yaml file")
    except Exception as e:
        raise AppException(e,sys)
    
def decodeImage(imgstring,filename):
    try:
        # 🔥 Remove metadata part
        if "base64," in imgstring:
            imgstring = imgstring.split("base64,")[1]
        imgdata = base64.b64decode(imgstring)
        with open(filename, 'wb') as f:
            f.write(imgdata)
        logging.info("Image decoded and saved successfully")
        print(f"Image decoded succesfully")
    except Exception as e:
        raise AppException(e,sys)
def encodeImageIntoBase64(croppedimagepath):
    with open(croppedimagepath,'rb') as f:
        return base64.b64encode(f.read())