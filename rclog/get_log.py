"""
rclog/get_log.py

"""

from logging import Logger, getLogger

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

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
