from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        outliers = [0]
        n = len(nums)
        for i in range(1,n):
            if(nums[i]%2==nums[i-1]%2):
                outliers.append(outliers[i-1]+1)
            else:
                outliers.append(outliers[i-1])
        res = []
        for l,r in queries:
            res.append(outliers[l]==outliers[r])
        return res