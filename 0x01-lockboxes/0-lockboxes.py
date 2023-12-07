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
    opened_boxes = set()
    opened_boxes.add(0)
    keys = boxes[0]
    while keys:
        key = keys.pop(0)
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])
    return len(opened_boxes) == len(boxes)
