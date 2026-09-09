class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp_x = x
        reversed_x = 0

        while temp_x > 0:
            last_digit = temp_x % 10
            reversed_x = (reversed_x * 10) + last_digit
            temp_x = temp_x // 10

        return reversed_x == x


# Time Complexity: O(d) where d is the number of digits
# Space Complexity: O(1)
