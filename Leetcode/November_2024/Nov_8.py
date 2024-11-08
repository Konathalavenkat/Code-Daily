from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res=[]
        xor=0
        for i in nums:
            xor^=i
            mask=1
            k=0
            for i in range(maximumBit):
                if(xor&mask==0):
                    k|=mask
                mask<<=1
            res.append(k)
        return res[::-1]