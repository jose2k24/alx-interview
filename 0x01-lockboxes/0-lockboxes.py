#!/usr/bin/python3
"""
Module for lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else False
    """
    if not boxes:
        return False

    n = len(boxes)
    keys = set(boxes[0])

    for key in keys:
        if key < n and key != 0:
            keys.update(boxes[key])

    return len(keys) == n
