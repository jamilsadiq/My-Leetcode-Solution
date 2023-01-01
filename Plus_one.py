from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(list(map(str,digits))))
        num2 = num+1
        res = [int(x) for x in str(num2)]
        return res
s= Solution()
#Case 1
print(s.plusOne([1,2,3])) #[1,2,4]
#Case 1
print(s.plusOne([4,3,2,1])) #[4,3,2,2]
#Case 1
print(s.plusOne([9])) #[1,0]