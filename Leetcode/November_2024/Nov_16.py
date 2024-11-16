from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res=[]
        cnt=1
        n=len(nums)
        for i in range(1,k):
            if(nums[i]-1 == nums[i-1]):
                cnt+=1
            else:
                cnt=1
        if(cnt>=k):
            res.append(nums[k-1])
        else:
            res.append(-1)
        for i in range(k,n):   
            if(nums[i]-1 == nums[i-1]):
                cnt+=1
            else:
                cnt=1
            if(cnt>=k):
                res.append(nums[i])
            else:
                res.append(-1)
        return res