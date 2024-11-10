from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if(k==0):
            return 1
        def getnum(bits):
            num=0
            for i in range(32):
                if(bits[i]>0):
                    num|=1<<i
            return num
        def addnumtobits(n,bits):
            res=0
            for i in range(32):
                if(n&1<<i):
                    bits[i]+=1
                if(bits[i]>0):
                    res|=1<<i
            return res
        def removenumfrombits(n,bits):
            res=0
            for i in range(32):
                if(n&1<<i):
                    bits[i]-=1
                if(bits[i]>0):
                    res|=1<<i
            return res
        left=0
        res = 1e9
        n=len(nums)
        curr=0
        bits=[0]*32
        for i in range(n):
            curr=addnumtobits(nums[i],bits)
            while(curr>=k):
                res=min(res,i-left+1)
                curr=removenumfrombits(nums[left],bits)
                left+=1
        return res if res!=1e9 else -1