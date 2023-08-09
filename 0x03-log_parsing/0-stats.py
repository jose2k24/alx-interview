#!/usr/bin/python3

python
"""
This module reads from standard input line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
- Total file size: File size: <total size>, where <total size> is the sum of all previous <file size>.
- Number of lines by status code:
  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
  - If a status code doesn’t appear or is not an integer, don’t print anything for this status code.
  - Format: <status code>: <number>
  - Status codes should be printed in ascending order.

Example usage:
$ cat input.txt | python metrics.py

"""

import sys

def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (counter == 10):
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)