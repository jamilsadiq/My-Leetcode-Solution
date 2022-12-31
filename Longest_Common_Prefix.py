from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        prefix = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break
        return prefix
s = Solution()
#case 1
print(s.longestCommonPrefix(["flower","flow","flight"])) # fl
#case 2
print(s.longestCommonPrefix(["dog","racecar","car"])) # ''