from CosmeticDetection.exception import AppException
import sys

try:
    a = 1/"as"
except Exception as e:
    raise AppException(e,sys)