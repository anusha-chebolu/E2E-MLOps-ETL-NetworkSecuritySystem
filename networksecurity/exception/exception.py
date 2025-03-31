import sys
import inspect

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message

        try:
            # Try to extract traceback info if inside an exception context
            _, _, exc_tb = error_details.exc_info()
            if exc_tb is not None:
                self.lineno = exc_tb.tb_lineno
                self.file_name = exc_tb.tb_frame.f_code.co_filename
            else:
                # Fallback if no exception context
                frame = inspect.currentframe().f_back
                self.lineno = frame.f_lineno
                self.file_name = frame.f_code.co_filename
        except:
            self.lineno = -1
            self.file_name = "Unknown"

    def __str__(self):
        return (
            f"Error occured in python script name [{self.file_name}] "
            f"line number [{self.lineno}] error message [{str(self.error_message)}]"
        )
