class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l,r = 1,max(nums)
        n = len(nums)
        def possible(mid):
            ops = 0
            for i in nums:
                if(i>mid):
                    ops+=math.ceil(i/mid)-1
            return ops<=maxOperations
        while(l<=r):
            mid = (l+r)//2
            if(possible(mid)):
                r=mid-1
            else:
                l=mid+1
        return l   