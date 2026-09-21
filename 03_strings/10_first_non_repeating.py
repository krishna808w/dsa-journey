def first_non_repeating(string):
  string_count={}
  for char in string:
    if(char.isalpha()):
      lower_char=char.lower()
      if(lower_char in string_count):
        string_count[lower_char]+=1
      else:
        string_count[lower_char]=1
  for key in string_count:
    if(string_count[key]==1):
      return key
  return None


print(first_non_repeating("leetcode"))        # l
print(first_non_repeating("loveleetcode"))    # v
print(first_non_repeating("aabbc"))            # c
print(first_non_repeating("aabb"))             # None
print(first_non_repeating("swiss"))            # w
print(first_non_repeating("Aabb"))             # None
print(first_non_repeating("a!a"))              # None

#Time Complexity : O(N+M)
#Space Complexity : O(1)