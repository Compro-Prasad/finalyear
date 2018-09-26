#!/usr/bin/env python3

# Question 1:
#  Give an optimal algorithm for the longest palindrome that is a
#  subsequence of the given input string.

# Example:
#  Input:
#   character
#  Output:
#   carac

def longest_common_subsequence(x, y):
    lenx = len(x) + 1
    leny = len(y) + 1
    matrix = []
    for i in range(leny):
        matrix += [[0] * lenx]
    for i in range(1, leny):
        for j in range(1, lenx):
            if x[j - 1] == y[i - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    for m in matrix:
        print(m)
    i = lenx - 1
    j = leny - 1
    a = ""
    while i != 0 and j != 0:
        if x[i - 1] == y[j - 1]:
            a += x[i - 1]
            i -= 1
            j -= 1
        else:
            if matrix[j][i - 1] > matrix[j - 1][i]:
                i -= 1
            else:
                j -= 1
    return a

def get_palindrome_subsequence(s):
    rev_s = s[::-1]
    return longest_common_subsequence(rev_s, s)

if __name__ == '__main__':
    s = input("Enter a string: ")
    print("Longest palindrome in subsequence is", get_palindrome_subsequence(s))
