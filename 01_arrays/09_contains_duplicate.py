def is_duplicate(num_arr):
  seen = set()
  for num in num_arr:
    if num in seen:
        return True

    seen.add(num)

  return False
print(is_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


# Time: O(n) average
# Space: O(n)