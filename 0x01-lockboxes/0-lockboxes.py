#!/usr/bin/python3
""" import module """


def canUnlockAll(boxes):
    """ ulock boxes """

    if (type(boxes)) is not list:
        return False
    arr = []
    arr.append(0)
    opened = []
    for box in boxes:
        for el in box:
            if el not in arr:
                arr.append(el)
        if not box:
            break
    for idx in arr:
        try:
            opened.append(boxes[idx])
        except:
            pass
    for i in opened:
        boxes.remove(i)
    return len(boxes) == 0
