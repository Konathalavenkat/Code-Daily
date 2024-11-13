from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        def lowerbound(nums,x):
            l,r=0,len(nums)-1
            res=0
            while(l<r):
                if(nums[l]+nums[r]<x):
                    res+=r-l
                    l+=1
                else:
                    r-=1
            return res
        return lowerbound(nums,upper+1)-lowerbound(nums,lower)
        


        # res=[0]
        # def upperbound(nums,x,l,r):
        #     while(l<=r):
        #         mid=(l+r)//2
        #         if(nums[mid]>x):
        #             r=mid-1
        #         else:
        #             l=mid+1
        #     return r+1
        # def lowerbound(nums,x,l,r):
        #     while(l<=r):
        #         mid=(l+r)//2
        #         if(nums[mid]>=x):
        #             r=mid-1
        #         else:
        #             l=mid+1
        #     return r+1
        # def mergesort(nums,l,r):
        #     if(l<r):
        #         mid=(l+r)//2
        #         mergesort(nums,l,mid)
        #         mergesort(nums,mid+1,r)
        #         merge(nums,l,mid,r)
        # def merge(nums,l,mid,r):
        #     # print(nums[l:mid+1],nums[mid+1:r+1],res[0])
        #     temp=[0]*(r-l+1)
        #     for i in range(mid+1,r+1):
        #         # print(nums[i],(upper-nums[i],upperbound(nums,upper-nums[i],l,mid)),(lower-nums[i],lowerbound(nums,lower-nums[i],l,mid)))
        #         res[0]+=upperbound(nums,upper-nums[i],l,mid)-lowerbound(nums,lower-nums[i],l,mid)
        #     # print(nums[l:mid+1],nums[mid+1:r+1],res[0])
        #     ind1,ind2,ind3=l,mid+1,0
        #     while(ind1<=mid and ind2<=r):
        #         if(nums[ind1]<nums[ind2]):
        #             temp[ind3]=nums[ind1]
        #             ind1+=1
        #         else:
        #             temp[ind3]=nums[ind2]
        #             ind2+=1
        #         ind3+=1
        #     while(ind1<=mid):
        #         temp[ind3]=nums[ind1]
        #         ind1+=1
        #         ind3+=1
        #     while(ind2<=r):
        #         temp[ind3]=nums[ind2]
        #         ind2+=1
        #         ind3+=1
        #     for i in range(l,r+1):
        #         nums[i]=temp[i-l]
        # mergesort(nums,0,len(nums)-1)
        # return res[0]

            
        



                