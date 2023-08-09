#!/usr/bin/python3

import sys

# Initialize variables
total_size = 0
status_codes = {}

# Read from standard input line by line
for i, line in enumerate(sys.stdin, start=1):
    # Parse the line and extract the status code and file size
    try:
        status_code = int(line.split()[8])
        file_size = int(line.split()[9])
    except (IndexError, ValueError):
        # Skip the line if it doesn't match the expected format
        continue

    # Update the total file size
    total_size += file_size

    # Update the number of lines by status code
    if status_code in status_codes:
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1

    # Print statistics after every 10 lines or a keyboard interruption
    if i % 10 == 0:
        print(f"Total file size: {total_size}")
        for code in sorted(status_codes):
            if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                print(f"{code}: {status_codes[code]}")
        print()
