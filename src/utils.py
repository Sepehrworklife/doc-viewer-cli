import os
from constants import SEC_FILE_NAME, MESSAGE_ERROR_IF_INITIAL_NOT_HAPPEND
from rich import print
from typer import Exit
from functools import wraps

def is_initial_happend(func):
    """Exit program if user has not set the personal token

    Args:
        func (_type_): _description_

    Raises:
        Exit: _description_

    Returns:
        _type_: _description_
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not os.path.exists(SEC_FILE_NAME):
            print(MESSAGE_ERROR_IF_INITIAL_NOT_HAPPEND)
            raise Exit()
        func(*args, **kwargs)
    return wrapper
        



