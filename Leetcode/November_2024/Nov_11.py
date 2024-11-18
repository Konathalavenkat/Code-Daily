from typing import List
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes=[]
        m=max(nums)
        n=len(nums)
        isprime=[True]*(m+1)
        isprime[0]=False
        isprime[1]=False
        for i in range(2,m+1):
            if(isprime[i]):
                primes.append(i)
                for j in range(i*i,m+1,i):
                    isprime[j]=False
        def lowerbound(n):
            l,r=0,len(primes)-1
            while(l<=r):
                mid=(l+r)//2
                if(primes[mid]<n):
                    l=mid+1
                else:
                    r=mid-1
            if(l==0):
                return 0
            return primes[l-1]
        nums[0]-=lowerbound(nums[0])
        for i in range(1,n):
            if(nums[i]<=nums[i-1]):
                print(nums)
                return False
            nums[i]-=lowerbound(nums[i]-nums[i-1])
        return True

