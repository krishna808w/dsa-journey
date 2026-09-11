def remove_duplicates(nums):
  unique_pointer=0
  current_pointer=1
  while current_pointer<len(nums):
    if(nums[current_pointer] != nums[unique_pointer]):
      nums[unique_pointer +1]=nums[current_pointer]
      unique_pointer+=1
    current_pointer+=1
  return nums[:unique_pointer+1]
print(remove_duplicates([1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([1, 2, 3, 4]))

#Time: O(n)
#Space: O(1) 