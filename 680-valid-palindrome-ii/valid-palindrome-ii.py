class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # If mismatch, we have used our "one deletion."
                # Check if skipping LEFT char makes a palindrome
                # OR if skipping RIGHT char makes a palindrome.
                
                skip_left = s[l+1 : r+1]  # Substring excluding l
                skip_right = s[l : r]     # Substring excluding r
                
                # Check if either resulting substring is a palindrome
                return (skip_left == skip_left[::-1]) or (skip_right == skip_right[::-1])
            
            # If they match, just move inward
            l += 1
            r -= 1
            
        return True