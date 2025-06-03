from typing import NoReturn
from os import _exit as close

# The error_stop() function
def error_stop(msg: str) -> NoReturn:
    """The `error_stop()` function allows the user to press the enter key
    before terminating the program with status `-1`.

    Args:
        msg (str): The message to display, after which, the following is appended on a new line: "`Press Enter to Exit.`"

    Returns:
        NoReturn: This function terminates the program.
    """
    # Display the message and prompt the user to press enter
    # to exit.
    input(msg + "\nPress Enter to Exit.\n")

    # Terminate the program.
    close(-1)
