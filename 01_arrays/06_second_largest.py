nums = [10, 5, 8, 20, 15]


def find_second_largest(nums):
    largest = nums[0]
    second_largest = float("-inf")

    for i in range(1, len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]

        elif nums[i] > second_largest and nums[i] < largest:
            second_largest = nums[i]

    return second_largest


print(find_second_largest(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)

def second_largest(num_arr):
  largest_num=num_arr[0]
  second_largest_num=None
  for num in num_arr:    
    if(num>largest_num ):
      second_largest_num=largest_num
      largest_num=num
    elif((second_largest_num is None or second_largest_num<num) and num!=largest_num):
      second_largest_num=num
  
    
  return second_largest_num

print(second_largest([10, 10, 8]))
print(second_largest([10, 10, 10]))
print(second_largest([-5, -2, -8, -1]))
print(second_largest([5]))

# Time Complexity: O(n)
# Space Complexity: O(1)