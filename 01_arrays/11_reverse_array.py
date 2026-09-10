def reverse_array(num_arr):
  left = 0
  right = len(num_arr) - 1
  while  left<right:
    swap_1=num_arr[left]
    swap_2=num_arr[right]
    num_arr[left]=swap_2
    num_arr[right]=swap_1
    left += 1
    right -= 1
    
  return num_arr

print(reverse_array([1, 2, 3, 4,5]))

#Time complexity : O(n)
#Space complexity : O(1)