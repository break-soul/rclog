"""
rclog/config_log.py
"""

from logging import config

from .env import check_debug
from .get_log import get_logger
from .trans import trans_config


def __config_log(*args, **kw) -> None:
    """
    日志配置根文件

        Args:
        config_dict (dict): 配置字典
    """
    try:
        config.dictConfig(trans_config(*args, **kw))
    except Exception as e:  # pylint: disable=broad-exception-caught
        logger = get_logger("rclog.SetLogger")
        logger.error(
            "Failed to set logging config: {error}\nData: {data}",
            error=e,
            data=(str(args) + str(kw)),
        )
        if check_debug():
            raise


def from_dict(config_dict: dict) -> None:
    """
    从字典初始化日志配置

    Args:
        config_dict (dict): 配置字典
    """
    __config_log(**config_dict)


def from_args(*args, **kw) -> None:
    """
    从函数参数初始化日志配置
    """
    __config_log(*args, **kw)


def from_object(obj: object) -> None:
    """
    从对象初始化日志配置

    Args:
        obj (object): 配置对象
    """
    config_dict = {}
    for key in dir(obj):
        if key.find("_") != 0:
            config_dict[key] = getattr(obj, key)
    __config_log(trans_config(**config_dict))
