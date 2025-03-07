class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes
        
        original = x
        reversed_x = 0
        
        while x > 0:
            digit = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + digit
        
        return original == reversed_x


        