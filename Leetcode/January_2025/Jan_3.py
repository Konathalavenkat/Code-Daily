from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        res , n = 0, len(nums)
        for i in range(n-1):
            left+=nums[i]
            right-=nums[i]
            if(left>=right):
                res+=1
        return res