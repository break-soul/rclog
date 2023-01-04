# -*- coding: utf-8 -*-
# TransCoding.py

def formatters(formatter_name:str,format:str,datefmt:str,**kw):
    
    return {formatter_name:{"format": format,"datefmt": datefmt}}

def handler(handler_class:str,formatter:str,level:str,**kw):
    if(handler_class is "logging.StreamHandler"):
        return {"class": handler_class,"formatter": formatter,"level": level}
    else:
        return {"class": handler_class,"formatter": formatter,"level": level,"filename": kw["filename"],"maxBytes": kw["maxBytes"],"backupCount": kw["backupCount"],"encoding": kw["encoding"]}


def trans_coding(LOG_FORMAT="<%(asctime)s>[%(levelname)s]%(name)s:%(message)s",
               DATA_FORMAT="%Y-%m-%d %H:%M:%S",
               CONSOLE=True,
               LOG_LEVEL="INFO",
               LOG_FILE="Temp/logs/info.log",
               LOG_FILE_MAX_SIZE=1048576,
               LOG_FILE_BACKUP_COUNT=3,
               ERROR_FILE="Temp/logs/error.log",
               ERROR_FILE_MAX_SIZE=1048576,
               ERROR_FILE_BACKUP_COUNT=3,
               ENCODING="utf8") -> dict:
    """
    解析日志配置

    Args:
        LOG_FORMAT (str, optional): 日志格式. Defaults to "<%(asctime)s>[%(levelname)s]%(name)s:%(message)s".
        DATA_FORMAT (str, optional): 日期格式. Defaults to "%Y-%m-%d %H:%M:%S".
        CONSOLE (bool, optional): 开启命令行. Defaults to True.
        LOG_LEVEL (str, optional): 日志文件等级. Defaults to "INFO".
        LOG_FILE (str, optional): 日志文件位置. Defaults to "Temp/logs/info.log".
        LOG_FILE_MAX_SIZE (int, optional): 日志文件大小. Defaults to 1048576.
        LOG_FILE_BACKUP_COUNT (int, optional): 日志文件计数. Defaults to 3.
        ERROR_FILE (str, optional): 错误文件地址. Defaults to "Temp/logs/error.log".
        ERROR_FILE_MAX_SIZE (int, optional): 错误文件大小. Defaults to 1048576.
        ERROR_FILE_BACKUP_COUNT (int, optional): 错误文件计数. Defaults to 3.
        ENCODING (str, optional): 编码. Defaults to "utf8".

    Returns:
        dict: logging config
    """
    config = {
        "version": 1,
        "disable_existing_loggers": "False",
        "formatters": dict(),
        "handlers": dict(),
        "loggers": {
            "root": {
                "handlers": []
            }
        }
    }
    config["version"] = 1
    config["disable_existing_loggers"] = "False"
    config["formatters"] = {
        "default": {
            "format": LOG_FORMAT,
            "datefmt": DATA_FORMAT
        }
    }
    config["loggers"]["root"]["level"] = "INFO"
    config["loggers"]["root"]["handlers"] = list()
    if (CONSOLE is True):
        config["handlers"]["console"] = {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO"
        }
        config["loggers"]["root"]["handlers"].append("console")
    if (LOG_LEVEL is not None):
        config["handlers"]["file"] = {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "level": LOG_LEVEL,
            "filename": LOG_FILE,
            "maxBytes": LOG_FILE_MAX_SIZE,
            "backupCount": LOG_FILE_BACKUP_COUNT,
            "encoding": ENCODING
        }
        config["loggers"]["root"]["handlers"].append("file")
    if (ERROR_FILE is not None):
        config["handlers"]["error_file"] = {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "level": "ERROR",
            "filename": ERROR_FILE,
            "maxBytes": ERROR_FILE_MAX_SIZE,
            "backupCount": ERROR_FILE_BACKUP_COUNT,
            "encoding": ENCODING
        }
        config["loggers"]["root"]["handlers"].append("error_file")
    return config

