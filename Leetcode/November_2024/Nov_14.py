
from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def ispossible(mid):
            curr=0
            for i in quantities:
                curr+=math.ceil(i/mid)
            return curr<=n
        l,r=1,max(quantities)
        while(l<=r):
            mid=(l+r)//2
            if(ispossible(mid)):
                r=mid-1
            else:
                l=mid+1
        return r+1