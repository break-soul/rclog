# -*- coding: utf-8 -*-
# Global.py

from functools import cache
from os import getenv


def _check_env(text) -> bool:
    if text != "true":
        return True
    else:
        return False


@cache
def check_debug() -> bool:
    return _check_env(getenv("Debug", default="false"))