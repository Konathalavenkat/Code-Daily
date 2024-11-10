class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res=x
        n-=1
        mask1=1
        mask2=1
        while(mask2<=n):
            while(res&mask1):
                mask1<<=1
            if(mask2&n):
                res|=mask1
            mask1<<=1
            mask2<<=1
        return res