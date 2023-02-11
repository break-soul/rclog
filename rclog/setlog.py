# -*- coding: utf-8 -*-
# rclog/setlog.py

from logging.config import dictConfig

from .env import check_debug
from .getlog import get_logger
from .trans import trans_config

logger = get_logger("rclog.SetLogger")


def from_dict(config_dict: dict):
    """
    从字典初始化日志配置

    Args:
        config_dict (dict): 配置字典
    """

    try:
        dictConfig(trans_config(**config_dict))
    except Exception as e:
        logger.error("Failed to set logging config: {error}\nData: {data}".format(error=e,
                                                                                  data=config_dict))
        if (check_debug() == True):
            raise


def from_args(*args, **kw):
    """
    从函数参数初始化日志配置
    """

    try:
        dictConfig(trans_config(*args, **kw))
    except Exception as e:
        logger.error("Failed to set logging config: {error}\nData: {data}".format(error=e,
                                                                                  data=(str(args) +
                                                                                        str(kw))))
        if (check_debug() == True):
            raise


def from_object(obj: object):
    """
    从对象初始化日志配置

    Args:
        obj (object): 配置对象
    """

    try:
        config_dict = dict()
        for key in dir(obj):
            if key.find("_") != 0:
                config_dict[key] = getattr(obj, key)
        dictConfig(trans_config(**config_dict))
    except Exception as e:
        logger.error("Failed to set logging config: {error}\nData: {data}".format(error=e,
                                                                                  data=obj))
        if (check_debug() == True):
            raise
