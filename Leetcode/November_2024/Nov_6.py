class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def getsetbits(n):
            res=0
            while(n):
                res+=n&1
                n>>=1
            return res
        n=len(nums)
        left=0
        prev=nums[0].bit_count()
        for i in range(n):
            bits=nums[i].bit_count()
            if(bits==prev):
                continue
            else:
                nums[left:i]=sorted(nums[left:i])
                prev=bits
                left=i
        nums[left:n]=sorted(nums[left:n])
        return sorted(nums)==nums