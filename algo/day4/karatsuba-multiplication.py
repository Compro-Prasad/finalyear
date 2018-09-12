#!/usr/bin/env python3

# Question:
#  Multiply two numbers using karatsuba's multiplication

import math

def count_digits(x):
    if (type(x) == int and x > 0):
        return len(str(x))
    print("count_digits: error: Not a positive number")

def split_num(x, n):
    s = str(x)
    return int(s[:n]), int(s[n:])

def fast_multiply(x, y):
    if (x < 10 or y < 10):
        return x * y
    max_digit_count = max(count_digits(x), count_digits(y))
    m2 = math.floor(max_digit_count / 2)
    high1, low1 = split_num(x, m2)
    high2, low2 = split_num(y, m2)
    z2 = fast_multiply(high1, high2)
    z0 = fast_multiply(low1, low2)
    z1 = fast_multiply(high1 + low1, high2 + low2)
    return z2 * (10 ** (m2 * 2)) + (z1 - z2 - z0) * (10 ** m2) + z0

if __name__ == '__main__'
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print("Fast multiply returned:", fast_multiply(x, y))
