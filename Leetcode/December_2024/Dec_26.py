from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(ind,target):
            if(ind == len(nums)):
                return 1 if target == 0 else 0
            if((ind,target) in memo):
                return memo[(ind,target)]
            memo[(ind,target)]=dp(ind+1,target-nums[ind])+dp(ind+1,target+nums[ind])
            return memo[(ind,target)]
        return dp(0,target)
