nums = [0, 1, 0, 3, 12]


def move_zeros(nums):
    position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position] = nums[i]
            position += 1

    for i in range(position, len(nums)):
        nums[i] = 0

    return nums


print(move_zeros(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
