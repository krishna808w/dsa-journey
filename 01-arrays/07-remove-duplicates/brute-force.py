nums = [5, 5, 5, 2, 2, 1]


def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result


print(remove_duplicates(nums))

# Time Complexity: O(n^2)
# Space Complexity: O(n)
