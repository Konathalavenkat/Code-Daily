from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        res=n-1
        left = 0 

        while(left < n and (left == 0 or arr[left]>=arr[left-1])):
            left+=1

        res = n - left 
        left-=1
        right = n-1
        while(right>left and (right == n-1 or arr[right]<=arr[right+1])):
            while(left>=0 and arr[left]>arr[right]):
                left-=1
            res = min(res,right - left - 1)
            right -= 1
        return res    
