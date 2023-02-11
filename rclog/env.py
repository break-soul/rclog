# -*- coding: utf-8 -*-
# rclog/env.py

from functools import lru_cache
from os import getenv


def _trans_env(text: str) -> bool:
    """
    get environment variable to bool

    Args:
        text (str): environment variable

    Returns:
        bool: environment variable to bool
    """
    if text == False :
        return False

    if text != "true" or text == True or text == "True":
        return True
    else:
        return False


@lru_cache
def check_debug() -> bool:
    """
    Check whether it is DEBUG mode

    Returns:
        bool: __debug__
    """

    return _trans_env(getenv("DEBUG", default=False))
