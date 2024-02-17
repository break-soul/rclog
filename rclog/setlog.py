# rclog/setlog.py

from logging.config import dictConfig

from .env import check_debug
from .getlog import get_log
from .trans import trans_config

logger = get_log("rclog.SetLogger")

def __config_log(*args, **kw):
    """
    日志配置根文件

        Args:
        config_dict (dict): 配置字典
    """
    try:
        dictConfig(trans_config(*args, **kw), force=True) # pylint: disable=unexpected-keyword-arg
    except Exception as e:  # pylint: disable=broad-except
        logger.error("Failed to set logging config: {error}\nData: {data}",
                     error=e,
                     data=(str(args) +str(kw)))
        if check_debug():
            raise

def from_dict(config_dict: dict):
    """
    从字典初始化日志配置

    Args:
        config_dict (dict): 配置字典
    """
    __config_log(**config_dict)



def from_args(*args, **kw):
    """
    从函数参数初始化日志配置
    """
    __config_log(*args, **kw)



def from_object(obj: object):
    """
    从对象初始化日志配置

    Args:
        obj (object): 配置对象
    """
    config_dict = dict()
    for key in dir(obj):
        if key.find("_") != 0:
            config_dict[key] = getattr(obj, key)
    __config_log(trans_config(**config_dict))
