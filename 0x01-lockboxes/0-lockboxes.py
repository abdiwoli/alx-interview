#!/usr/bin/python3
""" import module """


def canUnlockAll(boxes):
    """ ulock boxes """

    if (type(boxes)) is not list:
        return False
    arr = []
    arr.append(0)
    opened = []
    for n, box in enumerate(boxes):
        for el in box:
            if el not in arr and el != n:
                arr.append(el)
    for idx in arr:
        try:
            opened.append(boxes[idx])
        except IndexError:
            pass
    if opened == boxes:
        return True
    for i in opened:
        boxes.remove(i)
    return len(boxes) == 0
