# -*- coding: utf-8 -*-
# rclog/trans.py

from logging import INFO
from typing import Any,Optional

from .env import check_debug
from .io import mkdir

def dump_format(format_name: str = "default",
                **kw: dict[str, str]) -> dict[str, dict[str, str]]:
    """
    dump formatters

    Args:
        format_name (str): format name. Defaults to format.

    Keyword Args:
        format (str, optional): format.
        datefmt (str, optional): data format.

    Returns:
        dict[str, dict[str, str]]: logging dict config format
    """

    back_format = dict()
    if (format_name == "default"):
        back_format[
            "format"] = "<%(asctime)s>[%(levelname)s]%(name)s:%(message)s"
        back_format["datefmt"] = "%Y-%m-%d %H:%M:%S"
    else:
        back_format["format"] = kw["format"]
        back_format["datefmt"] = kw["datefmt"]
    return back_format



def dump_handler(handler_class: str,
                 formatter: str = "default",
                 level: Optional[str] = None,
                 **kw) -> dict[str, str]:
    """
    dump handlers

    Args:
        handler_class (str): log handler class
        formatter (str): log formatter. Defaults to "default".
        level (str | None): log level. Defaults to None.

    Keyword Args:
        filename (str, optional): log file name. Defaults to None.
        maxBytes (int, optional): log file max size. Defaults to None.
        backupCount (int, optional): log file backup count. Defaults to None.
        encoding (str, optional): log file encoding. Defaults to "utf8".

    Returns:
        dict[str, str]: logging dict config handler
    """
    back_handler = dict()

    # region trans handlers
    if (handler_class == "Console"):
        handler_class = "logging.StreamHandler"
    if (handler_class == "File"):
        handler_class = "logging.handlers.RotatingFileHandler"
    # endregion

    # region dump handlers
    back_handler["class"] = handler_class
    if (handler_class == "logging.NullHandler"):
        return back_handler

    back_handler["formatter"] = formatter
    if (level != None):
        back_handler["level"] = level
    if (back_handler["class"] == "logging.handlers.RotatingFileHandler"):
        if (kw["filename"] != None):
            back_handler["filename"] = kw["filename"]
            # if file mkdir
            match mkdir():
                case 10:
                    pass
                case 11:
                    pass
                case 21:
                    if check_debug():
                        raise Exception("make file dir is in error!")
        else :
            raise Exception("Filename is none!")

        back_handler["maxBytes"] = kw["maxBytes"]
        back_handler["backupCount"] = kw["backupCount"]
        back_handler["encoding"] = kw["encoding"]
        back_handler["encoding"] = "utf8"
    # endregion

    return back_handler


def trans_config(handlers: list,
                 formats: list = [
                     "default",
                 ],
                 exist_loggers: bool = True,
                 **kw) -> dict[str, Any]:
    """
    trans config

    Args:
        handlers (list): _description_
        formats (list, optional): _description_. Defaults to [ "default", ].
        exist_loggers (bool, optional): _description_. Defaults to True.

    Keyword Args:
        "{format_name}_format" (str, optional): _description_. Defaults to "<%(asctime)s>[%(levelname)s]%(name)s:%(message)s".
        "{format_name}_datefmt" (str, optional): _description_. Defaults to "%Y-%m-%d %H:%M:%S".
        "{handler_name}_class" (str, optional): _description_. Defaults to "Console".
        "{handler_name}_formatter" (str, optional): _description_. Defaults to "default".
        "{handler_name}_level" (str, optional): _description_. Defaults to None.
        "{handler_name}_filename" (str, optional): _description_. Defaults to None.
        "{handler_name}_maxBytes" (int, optional): _description_. Defaults to None.
        "{handler_name}_backupCount" (int, optional): _description_. Defaults to None.
        "{handler_name}_encoding" (str, optional): _description_. Defaults to "utf8".

    Returns:
        dict[str, Any]: _description_
    """

    # init config
    config = dict()
    config["version"] = 1
    config["formatters"] = dict()
    config["handlers"] = dict()
    config["loggers"] = dict()
    config["loggers"]["root"] = dict()
    config["loggers"]["root"]["handlers"] = list()

    # exist loggers
    if (exist_loggers is True):
        config["disable_existing_loggers"] = "False"
    else:
        config["disable_existing_loggers"] = "True"

    # formatters
    for format_name in formats:
        config["formatters"][format_name] = dump_format(
            format_name=format_name,
            format=kw.get(f"{format_name}_format"),  # type:ignore
            datefmt=kw.get(f"{format_name}_datefmt"))  # type:ignore

    # handlers
    for handler_name in handlers:
        config["handlers"][handler_name] = dump_handler(
            handler_class=kw.get(f"{handler_name}_class"),  # type:ignore
            formatter=kw.get(f"{handler_name}_formatter", "default"),
            level=kw.get(f"{handler_name}_level", INFO),
            filename=kw.get(f"{handler_name}_filename", "log.log"),
            maxBytes=kw.get(f"{handler_name}_maxBytes", 1048576),
            backupCount=kw.get(f"{handler_name}_backupCount", 3),
            encoding=kw.get(f"{handler_name}_encoding", "utf8"))
        config["loggers"]["root"]["handlers"].append(handler_name)

    return config
