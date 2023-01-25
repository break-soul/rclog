# -*- coding: utf-8 -*-
# GlobalHook.py

# Use to other modules to use global variables

from os import environ


def check_global() -> object | bool:
    """
    Check global variables

    Returns:
        bool: True if exists
    """
    try:
        from .. import Global
        return Global
    except:
        return False


check = check_global()


def get_global(var, default=None):
    """
    Get global variables

    Returns:
        dict: Global variables
    """
    if (check != False):
        return check.get_var(var, default)  # type: ignore
    return environ.get(var, default)


def set_global(key, value):
    """
    Set global variables

    Args:
        key (str): Key
        value (any): Value
    """
    if (check != False):
        check.set_var(key, value) # type: ignore
    environ.get[key] = value # type: ignore
