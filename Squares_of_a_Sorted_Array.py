from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list2=[]
        for val in nums:
            c =val*val
            list2.append(c)
        list2.sort()
        return list2
if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares(nums=[-4,-1,0,3,10]))
    print(s.sortedSquares(nums=[-7,-3,2,3,11]))