def find_longest_prefix(str_list):
  longest_prefix=""
  if(len(str_list)==0):
    return longest_prefix
  for j in range(len(str_list[0])):
    for i in range(1,len(str_list)):
      if j >= len(str_list[i]) or str_list[i][j] != str_list[0][j]:
        return longest_prefix
    longest_prefix+=str_list[0][j]
  return longest_prefix
  
        
       

print("1",find_longest_prefix(["flower", "flow", "flight"]))
print("2",find_longest_prefix(["dog", "racecar", "car"]))
print("3",find_longest_prefix(["flower", "flower"]))
print("4",find_longest_prefix([]))
print("5",find_longest_prefix([""]))



# Time Complexity: O(n * m)
# n = number of strings
# m = length of the shortest string
# Space Complexity: O(m)
