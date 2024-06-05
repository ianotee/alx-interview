#!/usr/bin/python3
"""Module for lockboxes"""


def canUnlockAll(boxes):
    """Checking the list of lists and the content
       of a list and unlocking other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
