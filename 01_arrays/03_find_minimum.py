nums = [4, 1, 7, 2, 9]


def find_minimum(nums):
    smallest = nums[0]

    for i in range(len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]

    return smallest


print(find_minimum(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
