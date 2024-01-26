#!/usr/bin/python3
'''
    Script that reads stdin line by line and computes metrics.
'''
import sys


def check_line(line):
    '''
        check_line: function
        @line: line of input to check
        return: True if it is validated.
                False otherwise.
    '''
    input_line = line.split(' ')
    if input_line[-1][-1] == '\n':
        input_line[-1] = input_line[-1][:-1]
    if input_line[-1].isdigit() and input_line[-2].isdigit():
        return True
    return False


def show_status_code_states(status_codes, files_total_size):
    '''
        show_status_code_states: function
        @status_codes: dictionary of status codes.
        return: void function
    '''
    print("File size: {}".format(files_total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{:s}: {:d}".format(code, status_codes[code]))


try:
    files_total_size = 0
    number_of_lines = 0
    status_codes_states = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    for line in sys.stdin:
        if check_line(line):
            file_size = line.split(' ')[-1]
            if file_size == '\n':
                file_size = file_size[:-1]
            status_code = line.split(' ')[-2]
            if status_code in sorted(status_codes_states.keys()):
                status_codes_states[status_code] += 1
            files_total_size += int(file_size)
        else:
            continue
        number_of_lines += 1
        if number_of_lines % 10 == 0:
            show_status_code_states(status_codes_states, files_total_size)
finally:
    show_status_code_states(status_codes_states, files_total_size)
