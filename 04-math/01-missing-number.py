nums = [3, 0, 1]


def find_missing(nums):
    array_sum = 0

    for i in range(len(nums)):
        array_sum += nums[i]

    expected_sum = (len(nums) * (len(nums) + 1)) // 2

    return expected_sum - array_sum


print(find_missing(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
