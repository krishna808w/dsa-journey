nums = [4, 1, 7, 2, 9]
target = 7


def contains_number(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return True

    return False


print(contains_number(nums, target))

# Time Complexity: O(n)
# Space Complexity: O(1)
