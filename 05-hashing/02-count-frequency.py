nums = [1, 2, 2, 3, 1, 4, 2]
target = 2


def find_frequency(nums, target):
    total_occurrence = 0

    for number in nums:
        if number == target:
            total_occurrence += 1

    return total_occurrence


print(find_frequency(nums, target))

# Time Complexity: O(n)
# Space Complexity: O(1)
