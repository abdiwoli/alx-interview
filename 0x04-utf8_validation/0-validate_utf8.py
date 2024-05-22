#!/usr/bin/python3
""" main function """


def validUTF8(data):
    """ determine utf8 """
    cont_bytes = 0
    if data is None:
        return False
    for byte in data:
        if cont_bytes == 0:
            if byte >> 5 == 0b110:
                cont_bytes = 1
            elif byte >> 4 == 0b1110:
                cont_bytes = 2
            elif byte >> 3 == 0b11110:
                cont_bytes = 3
            elif byte >> 7 != 0:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            cont_bytes -= 1

    return cont_bytes == 0
