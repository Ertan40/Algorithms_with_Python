"""
Write a program that finds the sum of all elements in an integer array. Use recursion.
Note: In practice, this recursion should not be used here (instead use an iterative solution), this is just an exercise.
examples:
input: 1 2 3 4    output: 10
input: -1 0 1    output: 0
"""


def calc_sum(nums, i):
    if i == len(nums) - 1:
        return nums[i]
    return nums[i] + calc_sum(nums, i + 1)


numbers = [int(num) for num in input().split()]
print(calc_sum(numbers, 0))