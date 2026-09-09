def validate_braces(braces_str):
  pairs = {
    ')': '(',
    '}': '{',
    ']': '['
  }
  stack = []
  for char in braces_str:
    if(char not in pairs):
      stack.append(char)
    elif stack and stack[-1] == pairs[char]:
      stack.pop()
    else:
      return False
  return len(stack)==0
        
       

print("1",validate_braces("({})"))
print("2",validate_braces("()[]{}"))
print("3",validate_braces("(]"))
print("4",validate_braces("([{}])"))
print("5",validate_braces("([)]"))
print("6",validate_braces("{"))
print("7",validate_braces(""))
print("8",validate_braces("()()()()"))
print("9",validate_braces("(((((())))))"))
print("10",validate_braces("(((((((((("))

# Time Complexity: O(n)
# Space Complexity: O(n)