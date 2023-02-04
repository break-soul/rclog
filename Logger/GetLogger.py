# -*- coding: utf-8 -*-
# GetLogger.py

from inspect import stack
from os.path import basename
from logging import Logger, getLogger

from typing import Optional


def get_logger(logger_name: Optional[str] = None) -> Logger:
    """
    获取日志对象

    Args:
        logger_name (str): If no name is specified, return the root logger.

    Returns:
        Logger: 日志对象
    """
    if (logger_name == None):
        logger_name = basename(stack()[1][1]).split(".")[0]
    return getLogger(logger_name)