#!/usr/bin/env python3

# Question:
#  Multiply two numbers using karatsuba's multiplication

from math import ceil, floor

def count_digits(x):
    if (type(x) == int and x > 0):
        return len(str(x))
    print("count_digits: error: Not a positive number")

def split_num(x, n):
    return int(floor(x / 10 ** n)), int(x % 10 ** n)

def fast_multiply(x, y):
    if (x < 10 and y < 10):
        return x * y
    max_digit_count = max(count_digits(x), count_digits(y))
    m2 = int(ceil(max_digit_count / 2))
    high1, low1 = split_num(x, m2)
    high2, low2 = split_num(y, m2)
    z2 = fast_multiply(high1, high2)
    z0 = fast_multiply(low1, low2)
    z1 = fast_multiply(high1 + low1, high2 + low2) - z2 - z0
    return int((z2 * (10 ** (m2 * 2))) + (z1 * (10 ** m2)) + z0)

if __name__ == '__main__':
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print("Fast multiply returned:", fast_multiply(x, y))
