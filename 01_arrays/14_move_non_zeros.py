def move_zeros(nums):
  
  last_non_zero_index=0
  current_index=0
  while current_index<len(nums):
    if(nums[current_index]!=0):
      swap_num=nums[last_non_zero_index]
      nums[last_non_zero_index]=nums[current_index]
      nums[current_index]=swap_num
      last_non_zero_index+=1
      
    
    current_index+=1
  return nums
    
print(move_zeros([0, 0, 0]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 1]))
print(move_zeros([1, 0]))
print(move_zeros([1, 0, 2, 0, 3]))