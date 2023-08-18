import sys
import logging
from src import logger



def error_message_detail(error, error_details: sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred In Python Script [{0}] line number [{1}] Error Message [{2}]".format(
      file_name,exc_tb.tb_lineno  , str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_massage, error_detail:sys) :
        super().__init__(error_massage)
        self.error_message = error_message_detail(error_massage, error_details=error_detail)
        
    def __str__(self):
        return self.error_message

#if __name__ == "__main__":
    #try:
    #    a = 1/0
    #except Exception as e :
        #logger.logging.info("Division by Zero Error")
        #logging.info("Division by Zero Error")
        #e = CustomException(e,sys)
        #logger.logging.info(e)
        #print(CustomException(e,sys)) 
        #raise CustomException(e,sys)
        #logger.logging.info(CustomException(e,sys))
    

