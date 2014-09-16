"""
http://www.spoj.com/problems/FCTRL/

A program to print the count trailing zeros from the factorial of N (N!)

For any positive integer N, Z(N) is the number of zeros at the end of the
decimal form of number N!.

Input:

    There is a single positive integer T on the first line of input (equal to
    about 100000). It stands for the number of numbers to follow. Then there
    are T lines, each containing exactly one positive integer number
    N, 1 <= N <= 1000000000.

Output:

    For every number N, output a single line containing the single
    non-negative integer Z(N).

Example:

    Sample Input
        6
        3
        60
        100
        1024
        23456
        8735373

    Sample Output
        0
        14
        24
        253
        5861
        2183837
"""
import fileinput
import math
import pdb

"""
This naive implementation is really slow.
"""
def Z(N):
    if(N == 1):
        return 1
    prod = N
    while(N >= 1):
        if(N == 1):
            prod = prod * N
        else:
            prod = prod * (N - 1)
        N -= 1
    return prod


for line in fileinput.input():
    lineno = fileinput.filelineno()
    zeros = 0
    if(lineno == 1):
        T = int(line)
    elif(lineno - 1 <= T and T != 0):
        N = int(line)
        result = math.factorial(N)
        for char in reversed(str(result)):
            if(char == '0'):
                zeros += 1
            else:
                break
        print("{0}".format(zeros))
