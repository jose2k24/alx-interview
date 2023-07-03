#!/usr/bin/python3
"""
This script generates the Pascal's triangle of 5 and prints it out.
"""

def pascal_triangle(n):
    """
    Generate the Pascal's triangle of n.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def print_triangle(triangle):
    """
    Print the Pascal's triangle in a formatted way.
    """
    for row in triangle:
        # Convert each element in the row to a string and join them with commas
        row_str = ",".join([str(x) for x in row])
        # Print the row in square brackets
        print("[{}]".format(row_str))

if __name__ == "__main__":
    # Call the pascal_triangle function with n=5 and print the result
    triangle = pascal_triangle(5)
    print_triangle(triangle)