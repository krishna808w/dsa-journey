nums = [5, 5, 5, 2, 2, 1]


def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


print(remove_duplicates(nums))

# Time Complexity: O(n) average
# Space Complexity: O(n)
