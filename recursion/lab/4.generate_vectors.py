"""
Generate all n-bit vectors of 0 and 1 in lexicographic order.
"""


def generate_vectors(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        generate_vectors(index + 1, vector)


n = int(input())
vector = [0] * n

generate_vectors(0, vector)

# Output:
# 3
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111