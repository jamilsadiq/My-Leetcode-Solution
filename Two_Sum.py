from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, num in enumerate(nums):
            if num in diffs:
                return [diffs[num], i]
            diffs[target - num] = i
        return []

# Tests
s = Solution()
#case 1
print(s.twoSum([2,7,11,15], 9)) #[0,1]
#Case 2
print(s.twoSum([3, 2, 4], 6)) #[1,2]
#Case 3
print(s.twoSum([3, 3], 6)) #[0,1]
