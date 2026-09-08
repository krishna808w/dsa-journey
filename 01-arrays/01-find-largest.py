nums = [4, 1, 7, 2, 9]


def find_largest(nums):
    largest = nums[0]

    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]

    return largest


print(find_largest(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
