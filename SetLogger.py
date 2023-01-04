# -*- coding: utf-8 -*-
# SetLogger.py

from logging.config import dictConfig

from .GetLogger import get_logger
from .TransCoding import trans_coding

logger = get_logger("Logger.SetLogger")

def from_object(obj: object):
    """
    从对象初始化日志配置

    Args:
        obj (object): 配置对象
    """    

    try:
        from .ImportString import import_string
        config_dict = dict()
        if isinstance(obj, str):
            log_config = import_string(obj)
        for key in dir(log_config):
            if key.isupper():
                config_dict[key] = getattr(log_config, key)
        dictConfig(trans_coding(**config_dict))
    except Exception as e:
        logger.error("Failed to set logging config: %s" % e)

def from_dict(config_dict: dict):
    """
    从字典初始化日志配置

    Args:
        config_dict (dict): 配置字典
    """    

    try:
        dictConfig(trans_coding(**config_dict))
    except Exception as e:
        logger.error("Failed to set logging config: %s" % e)
