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
    index = 0
    while index < len(data):
        if not isinstance(data[index], int) or data[index] < 0:
            return False
        first_bytes = format(data[index], '08b')[0:5]
        if first_bytes[0] == '0':
            pass
        else:
            match = re.search(r'1+', first_bytes)
            len_match = len(match.group())
            if len_match < 2 or len_match > 4:
                return False
            for i in range(1, len_match):
                if data[index + i] & 0b10000000 != 0b10000000:
                    return False
            index += len_match - 1
        index += 1
    return True
