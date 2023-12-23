#!/usr/bin/python3

import sys

total_file_size = 0
status_codes = {}

for line in sys.stdin:
    ip_address, date, method, status_code, file_size = line.strip().split()
    file_size = int(file_size)

    if status_code not in status_codes:
        status_codes[status_code] = 0

    total_file_size += file_size
    status_codes[status_code] += 1

    if len(status_codes) == 10 or sys.stdin.is_interrupted(sys.stdin.fileno()):
        print("Total file size: {}, File size: {}".format(total_file_size, file_size))
        print("Number of lines by status code:")
        for status_code, count in status_codes.items():
            if count > 0:
                print("{}: {}".format(status_code, count))
        sys.exit()