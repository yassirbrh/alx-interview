#!/usr/bin/python3
'''
    Script that reads stdin line by line and computes metrics.
'''
import copy
import re
import sys


def check_line(line):
    '''
        check_line: function
        @line: line of input to check
        return: True if it is validated.
                False otherwise.
    '''
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+')
    date = re.findall(r'\[(.*?)\]', line)
    status = re.findall(r'"(.*?)"', line)
    input_line = line.split(' ')
    if len(input_line) != 9:
        return False
    if input_line[8][-1] == '\n':
        input_line[8] = input_line[8][:-1]
    if not ip_pattern.match(input_line[0]):
        return False
    if not date_pattern.match(date[0]):
        return False
    if status[0] != 'GET /projects/260 HTTP/1.1':
        return False
    if not input_line[8].isdigit() or not input_line[7].isdigit():
        return False
    return True


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
            file_size = line.split(' ')[8]
            if file_size == '\n':
                file_size = file_size[:-1]
            status_code = line.split(' ')[7]
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
