def is_palindrome(string):
  filtered_string=''
  for char in string:
    if(char.isalnum()):
      filtered_string+=char.lower()
  return filtered_string ==filtered_string[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))
print(is_palindrome("a"))