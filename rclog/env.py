# -*- coding: utf-8 -*-
# Global.py

from os import getenv
from functools import lru_cache


def _check_env(text) -> bool:
    if text != "true":
        return True
    else:
        return False


@lru_cache
def check_debug() -> bool:
    return _check_env(getenv("Debug", default="false"))
