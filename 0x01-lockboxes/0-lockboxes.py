#!/usr/bin/python3
'''
    Method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
        canUnlockAll: Function
        boxes: array of boxes.
        return: True if openable, False otherwise
    '''
    boxes_to_open = list(range(1, len(boxes)))
    boxes_to_check = boxes[0]
    for key in boxes_to_check:
        if key in boxes_to_open:
            boxes_to_open.remove(key)
        for boxkey in boxes[key]:
            if boxkey not in boxes_to_check:
                boxes_to_check.append(boxkey)
    if len(boxes_to_open) == 0:
        return True
    return False
