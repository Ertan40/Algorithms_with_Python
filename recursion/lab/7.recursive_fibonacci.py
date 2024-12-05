## iteration is faster
def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


n = int(input())
print(iterative_fib(n))


# def get_fibonacci(n):
#     if n < 0:
#         print("Please enter a positive number")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return get_fibonacci(n - 1) + get_fibonacci(n - 2)
#
#
# # the same value is calculated many, many times
# number = int(input())
# print(get_fibonacci(number))


