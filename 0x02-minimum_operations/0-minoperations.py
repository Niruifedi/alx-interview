#!/usr/bin/python3
"""
minimum operation
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in H
    """

    h = 1
    op = 0
    counter = 0

    while h < n:
        if op == 0:
            op = h
            counter += 1

        if h == 1:
            h += op
            counter += 1
            continue

        remaining = n - h

        if remaining < op:
            return 0

        if remaining % h != 0:
            h += op
            counter += 1
        else:
            op = h
            h += op
            counter += 2

    if h == n:
        return counter
    else:
        return 0
