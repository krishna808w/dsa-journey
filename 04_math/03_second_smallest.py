nums = [4, 1, 1, 9]


def find_second_smallest(nums):
    smallest_number = nums[0]
    second_smallest_number = float("inf")

    for i in range(len(nums)):
        if nums[i] < smallest_number:
            second_smallest_number = smallest_number
            smallest_number = nums[i]

        elif nums[i] < second_smallest_number and nums[i] > smallest_number:
            second_smallest_number = nums[i]

    return second_smallest_number


print(find_second_smallest(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
