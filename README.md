# rclog
![PyPI](https://img.shields.io/pypi/v/rclog)
![PyPI - License](https://img.shields.io/pypi/l/rclog)

![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/break-soul/rclog/python-package.yml?label=build)

Packaging to the logging module in python

# Interface
Provide `set_log` and` get_log`

## `set_log`
`set_log` can be configured in various ways, and there are the following configuration options:

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

## `get_log`
The `get_log` function can get the` logger` object, you can set the name, the file name that the default is called
