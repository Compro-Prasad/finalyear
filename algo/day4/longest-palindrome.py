#!/usr/bin/env python3

# Question 1:
#  Give an optimal algorithm for the longest palindrome that is a
#  subsequence of the given input string.

# Example:
#  Input:
#   character
#  Output:
#   carac

def find_next_match(x, i, y, j):
    while i < len(x):
        k = j
        while k < len(y):
            if (x[i] == y[k]):
                print(x, i, y, k)
                return i, k
            k += 1
        i += 1

def longest_common_substring(x, y):
    i = 0
    j = 0
    z = ""
    while i < len(x) and j < len(y):
        m, n = find_next_match(x, i, y, j)
        b, a = find_next_match(y, i, x, j)
        if i > a:
            i, j = a, b
        else:
            i, j = m, n
        z += x[i]
        i += 1
        j += 1
    return z

def get_palindrome_subsequence(s):
    rev_s = s[::-1]
    return longest_common_substring(s, rev_s)

if __name__ == '__main__':
    s = input("Enter a string: ")
    print("Longest palindrome in subsequence is", get_palindrome_subsequence(s))
