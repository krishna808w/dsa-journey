class Solution:
  def romanToInt(self, s: str) -> int:
    roman_conversion={
     'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
    }

    roman_pre=['I','X','C','M']
    result=0
    i=0
    while i<len(s):
      if(i != len(s) - 1 and roman_conversion[s[i+1]]> roman_conversion[s[i]]):
          calc=roman_conversion[s[i+1]] - roman_conversion[s[i]]
          result+=calc
          i+=2
      else:
          result+=roman_conversion[s[i]]
          i+=1
    return result

solution=Solution()
print(solution.romanToInt("MCMXCIV"))

# Time Complexity: O(n)
# Space Complexity: O(1)