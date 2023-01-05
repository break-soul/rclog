# -*- coding: utf-8 -*-
# GetLogger.py

from inspect import currentframe
import logging


def get_logger(logger_name: str | None = currentframe().f_back.f_code.co_filename) -> logging.Logger:
    """
    获取日志对象

    Args:
        logger_name (str): If no name is specified, return the root logger.

    Returns:
        logging.Logger: 日志对象
    """
    return logging.getLogger(logger_name)