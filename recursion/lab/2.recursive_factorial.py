"""
Write a program that calculates the recursively factorial of a given number.
NOTE: In practice, this recursion should not be used here (instead use an iterative solution).
"""


def find_recursive_factorial(n):
    if n == 0:
        return 1
    return n * find_recursive_factorial(n - 1)  # 3! = 3 * 2!


n = int(input())
print(find_recursive_factorial(n))