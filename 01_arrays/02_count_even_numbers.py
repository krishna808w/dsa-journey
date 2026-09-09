nums = [1, 2, 3, 4, 5, 6]


def count_even(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1

    return count


print(count_even(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)
