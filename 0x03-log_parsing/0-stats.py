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

def compute_metrics():
    """
    Reads from standard input line by line and computes metrics.
    """
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

if __name__ == "__main__":
    compute_metrics()