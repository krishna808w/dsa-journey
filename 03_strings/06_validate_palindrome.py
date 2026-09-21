def is_palindrome(word):
  p1=0
  p2=len(word)-1
  while p1 < p2:
    if(not word[p1].isalnum()):
      p1+=1
      continue
    if(not word[p2].isalnum()):
      p2-=1
      continue
      
    if(word[p1].lower()!=word[p2].lower()):
      return False
    p1+=1
    p2-=1
  return True

print(is_palindrome("Racecar"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(""))
print(is_palindrome("a"))
print(is_palindrome(".,"))

#Time Complexity : O(n) where n is the length of the string.
#Space Complexity : O(1)