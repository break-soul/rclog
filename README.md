# rclog
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

对python中logging模块的包装

# 接口
对外提供`SetLogger`和`get_logger`

## `SetLogger`
`SetLogger` 内有from_dict,from_args,from_object多个函数，可用多种方式配置log，有下列配置选项


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

## `get_logger`
`get_logger`函数可以获取`Logger`对象，可以设置名字，默认为调用的文件名
