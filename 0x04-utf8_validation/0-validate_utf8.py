#!/usr/bin/python3
'''
    Method that determines if a given data set represents a valid UTF-8
    encoding.
'''
from typing import List
import re


def validUTF8(data: List[int]) -> bool:
    '''
        validUTF8: function
        @data: data to check (it is represented as list of integers).
        return: True if the data is UTF-8 valid.
                False if the data not UTF-8 valid.
    '''
    if data is None or not isinstance(data, list):
        return False
    i = 0
    while i < len(data):
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 0x10FFFF:
            return False
        first_bytes = format(data[i], '08b')[0:5]
        if first_bytes[0] == '0':
            i += 1
            continue
        else:
            match = re.search(r'1+', first_bytes)
            len_match = len(match.group())
            if len_match < 2 or len_match > 4:
                return False
            for index in range(1, len_match):
                if data[index + i] & 0b10000000 != 0b10000000:
                    return False
            i += len_match
    return True
