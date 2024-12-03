def reverse_array(idx, numbers):
    if idx == len(numbers) // 2:
        return
    swap_idx = len(numbers) - 1 - idx
    numbers[idx], numbers[swap_idx] = numbers[swap_idx], numbers[idx]
    reverse_array(idx + 1, numbers)


nums = input().split()
reverse_array(0, nums)
print(' '.join(nums))



