"""
Write a program that simulates the execution of n nested loops from 1 to n which prints the values of all its 
iteration variables at any given time on a single line. Use recursion.
"""
def nested_loops(idx, array):
    if idx >= len(array):
        print(*array, sep=' ')
        return

    for num in range(1, len(array) + 1):
        array[idx] = num
        nested_loops(idx + 1, array)


n = int(input())
array = [None] * n
nested_loops(0, array)

