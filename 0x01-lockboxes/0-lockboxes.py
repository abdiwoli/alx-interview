#!/usr/bin/python3
""" import module """


def canUnlockAll(boxes):
    """ ulock boxes """

    if (type(boxes)) is not list:
        return False
    ln = len(boxes)
    opened = []
    opened.append(boxes[0])
    if ln == 0:
        return False
    for box in boxes:
        if (not box):
            opened.append(box)
            break
        for i in box:
            if i < ln and i > 0:
                if box not in opened:
                    opened.append(box)
                else:
                    break
    for box in opened:
        boxes.remove(box)
    return len(boxes) == 0
