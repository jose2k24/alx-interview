#!/usr/bin/python3
"""
A script for lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list): A list of lists of integers 
    representing the boxes and their keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    keys = set(boxes[0])

    for key in keys:
        if key < n and key != 0:
            keys.update(boxes[key])
    return len(keys) == n
