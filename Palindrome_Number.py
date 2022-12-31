class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = s[::-1]
        if r == s:
            return True
        else:
            return False 
s = Solution()
#case 1
print(s.isPalindrome(121)) #true
#case 2
print(s.isPalindrome(-121)) #false
#case 3
print(s.isPalindrome(10)) #false