"""
rclog/exception.py
"""


class MakeDirError(Exception):
    """
    Error
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
