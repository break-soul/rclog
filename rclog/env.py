"""
rclog/env.py
"""

from functools import lru_cache
from os import getenv

from typing import Union


def _trans_env(text: Union[str, bool]) -> bool:
    """
    get environment variable to bool

    Args:
        text (str): environment variable

    Returns:
        bool: environment variable to bool
    """
    if text is False:
        return False
    if text != "true" or text is True or text == "True":
        return True
    return False


@lru_cache
def check_debug() -> bool:
    """
    Check whether it is DEBUG mode

    Returns:
        bool: __debug__
    """

    return _trans_env(getenv("DEBUG", default=""))
