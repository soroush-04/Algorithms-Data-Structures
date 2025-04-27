"""
Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

from typing import List, Optional


def happy_number(n: int) -> bool:
    def check_next(next):
        sum_digits = 0

        while next > 0:
            digit = next % 10
            sum_digits += digit**2
            next //= 10

        return sum_digits

    seen = set()

    while True:
        if n == 1:
            return print(True)
        if n in seen:
            return print(False)

        seen.add(n)
        n = check_next(n)


happy_number(19)
