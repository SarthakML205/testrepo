from src.mlproject.logging import logging 
from src.mlproject.exception import CustomExpection
import sys 

if __name__ == "__main__":
    logging.info("the execution has started")
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("custom exception")
        raise CustomExpection(e, sys)