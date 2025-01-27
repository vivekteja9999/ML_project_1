import sys
import logging

def error_message_detail(error , error_detail:sys):
    _,_,error_at_where_details=error_detail.exc_info()
    file_name=error_at_where_details.tb_frame.f_code.co_filename
    line_no=error_at_where_details.tb_lineno
    error_message=f"Error occurred in the python script in {file_name} at line {line_no} , error is {str(error)}"
    return error_message

#we can use just sys also, here we are using error_details as a name instead of sys
class CustomException(Exception):
    def __init__(self , error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message , error_detail=error_details)

    def __str__(self):
        return self.error_message
        
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error")
        CustomException(e , sys)

