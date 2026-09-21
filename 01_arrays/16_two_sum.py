def two_sum(nums, target):
    hash_map={}
    for i in range(len(nums)):
      required=target-nums[i]
      if(required in hash_map):
        return [hash_map[required],i]
      else:
        hash_map[nums[i]]=i
    return None


print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))      # [0, 1]
print(two_sum([1, 2, 3], 10))      # None
print(two_sum([-1, -2, -3, -4], -6))  # [1, 3]

#Time Complexity : O(N)
#Space Complexity : O(N)