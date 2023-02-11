# -*- coding: utf-8 -*-
# rclog/io.py


from os import makedirs, path
from pathlib import Path


def mkdir(file_path: str) -> int:
    """
    make log file dirs

    Args:
        file_path (str): file path

    Returns:
        int: status
    """    

    dir_path = Path(file_path).parent
    if path.isdir(dir_path):
        return 11
    try:
        makedirs(dir_path)
    except:
        return 20
    return 10
