def two_sum(num_array, target):
  seen={}
  for i in range(len(num_array)):
    if target - num_array[i] in seen:
        return [i, seen[target - num_array[i]]]

    seen[num_array[i]] = i

print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))      # [0, 1]
print(two_sum([1, 2, 3], 10))      # None
print(two_sum([-1, -2, -3, -4], -6))  # [1, 3]



#Time: O(n) average
#Space: O(n)