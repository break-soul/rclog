"""
rclog/get_log.py

"""

from typing import Union
from logging import Logger, getLogger


def get_logger(logger_name: Union[str, None] = None) -> Logger:
    """
    Get the logging object

    Args:
        logger_name (str): If no name is specified, return the root logger.

    Returns:
        Logger: logging object
    """

    if logger_name is None:
        logger_name = "root"
    return getLogger(logger_name)
