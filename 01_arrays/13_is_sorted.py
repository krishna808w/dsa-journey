def is_sorted(nums):
  if(len(nums)<=1):
      return True
  i=1
  while i<len(nums):
    if(nums[i-1] > nums[i]):
      return False
    i+=1
  return True
    
print(is_sorted([1, 1, 2, 2, 3, 3, 4]))
print(is_sorted([1, 2, 3, 4]))
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 2, 2, 3, 4]))
print(is_sorted([1, 3, 2, 4, 5]))
print(is_sorted([5]))
print(is_sorted([]))