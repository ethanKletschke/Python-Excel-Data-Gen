from typing import NoReturn
from os import _exit as close

def error_stop(msg: str) -> NoReturn:
    input(msg + "\nPress Enter to Exit.\n")
    close(-1)
    
