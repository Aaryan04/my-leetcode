class Solution:
    def isPalindrome(self, x: int) -> bool:
        # condn when x is negative or x ends with 0 it needs to start with 0 which is possible for only one number : zero
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = (rev * 10) + (x % 10)            # updating reversed num 
            x = x // 10         # update x removing units place
        
        return x == rev or x == rev // 10