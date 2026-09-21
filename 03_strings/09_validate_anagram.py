def is_anagram(str1,str2):
  str1_count={}
  str2_count={}
  for char in str1:
    if(char.isalpha()):
      lower_char=char.lower()
      if(lower_char in str1_count):
        str1_count[lower_char]+=1
      else:
        str1_count[lower_char]=1
  for char in str2:
    if(char.isalpha()):
      lower_char=char.lower()
      if(lower_char in str2_count):
        str2_count[lower_char]+=1
      else:
        str2_count[lower_char]=1
  if(len(str1_count)!=len(str2_count)):
    return False
  else:
    for key in str1_count:
      if(str1_count[key]!=str2_count[key]):
        return False
  return True


print(is_anagram("listen", "silent"))           # True
print(is_anagram("hello", "world"))             # False
print(is_anagram("Listen!", "silent"))          # True
print(is_anagram("abc", "abcd"))                # False
print(is_anagram("ab", "aa"))                   # False
print(is_anagram("abc123", "abc"))              # True
print(is_anagram("A gentleman", "Elegant man")) # True

#Time Complexity : O(N+M)
#Space Complexity : O(1)