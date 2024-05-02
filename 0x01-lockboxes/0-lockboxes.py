#!/usr/bin/python3
""" import module """


def canUnlockAll(boxes):
    """ ulock boxes """
    idx = 0
    ln = len(boxes)
    opened = set()
    opened.add(0)
    if ln <= 0:
        return False
    for box in boxes:
        if (not box):
            break
        for i in box:
            if i < ln:
                opened.add(i)
    print(opened)
    if len(opened) == ln:
        return True
    return False
