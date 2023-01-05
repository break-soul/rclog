# -*- coding: utf-8 -*-
# GlobalHook.py

# Use to other modules to use global variables

from os import environ


def check_global() -> bool:
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
    if (check):
        return check.get_global_var(var, default)
    return environ.get(var, default)


def set_global(key, value):
    """
    Set global variables

    Args:
        key (str): Key
        value (any): Value
    """
    if (check):
        check.get_global_dict[key] = value
    environ.get[key] = value
