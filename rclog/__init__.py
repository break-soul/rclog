"""
rclog/__init__.py

set_log can be configured in various ways, and there are the following configuration options:

    Args:
        handlers (list):_description_
        formats (list, optional): _description_. Defaults to [ "default", ].
        exist_loggers (bool, optional): _description_. Defaults to True.

    Keyword Args:
        "{format_name}_format" (str, optional):_description_. 
            Defaults to "<%(asctime)s>[%(levelname)s]%(name)s:%(message)s".
        "{format_name}_datefmt" (str, optional): _description_. Defaults to "%Y-%m-%d %H:%M:%S".
        "{handler_name}_class" (str, optional): _description_. Defaults to "Console".
        "{handler_name}_formatter" (str, optional): _description_. Defaults to "default".
        "{handler_name}_level" (str, optional): _description_. Defaults to None.
        "{handler_name}_filename" (str, optional): _description_. Defaults to None.
        "{handler_name}_maxBytes" (int, optional): _description_. Defaults to None.
        "{handler_name}_backupCount" (int, optional): _description_. Defaults to None.
        "{handler_name}_encoding" (str, optional): _description_. Defaults to "utf8".
"""

from . import config_log as set_log
from .get_log import get_logger as get_log
