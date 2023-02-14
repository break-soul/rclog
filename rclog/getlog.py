# -*- coding: utf-8 -*-
# rclog/getlog.py


from inspect import stack
from os.path import basename
from logging import Logger, getLogger



def get_log(logger_name: str|None = None) -> Logger:
    """
    Get the logging object

    Args:
        logger_name (str): If no name is specified, return the root logger.

    Returns:
        Logger: logging object
    """
    
    if (logger_name == None):
        logger_name = basename(stack()[1][1]).split(".")[0]
    return getLogger(logger_name)
