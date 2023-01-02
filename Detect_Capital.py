class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(65<=ord(i)<=90 for i in word):
            return True
        if all(97<=ord(i)<=122 for i in word):
            return True
        if 65<=ord(word[0])<=90 and all(97<=ord(i)<=122 for i in word[1:]):
            return True
        else:
            return False
if __name__ == '__main__':
    s = Solution()
    #case 1
    print(s.detectCapitalUse(word = "USA")) #true
    #case 2
    print(s.detectCapitalUse(word = "FlaG")) #false

