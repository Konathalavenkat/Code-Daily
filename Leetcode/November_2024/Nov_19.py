from typing import List 
from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res=0
        d=defaultdict(int)
        cnt=0
        prefix = 0
        
        for i in range(k):
            if(d.get(nums[i],0)==0):
                cnt+=1
            d[nums[i]]+=1
            prefix += nums[i]
        if(cnt ==k):
            res = prefix
        
        for i in range(k,len(nums)):
            if(d.get(nums[i-k])==1):
                cnt-=1
            d[nums[i-k]]-=1
            if(d.get(nums[i],0)==0):
                cnt+=1
            d[nums[i]]+=1
            prefix+=nums[i]-nums[i-k]
            if(cnt == k):
                res = max(res, prefix)
        return res
