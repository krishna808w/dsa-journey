nums = [10, 5, 8, 20, 15]


def find_second_largest(nums):
    largest = nums[0]
    second_largest = float("-inf")

    for i in range(1, len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]

        elif nums[i] > second_largest and nums[i] < largest:
            second_largest = nums[i]

    return second_largest


print(find_second_largest(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
