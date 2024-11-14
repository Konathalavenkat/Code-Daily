from heapq import heappush,heappop
class Solution:
    def nearlySorted(self, arr, k):
        #code
        heap=[]
        n=len(arr)
        ind=0
        for i in range(k+1):
            heappush(heap, arr[i])
        for i in range(k+1,n):
            arr[ind]=heappop(heap)
            heappush(heap,arr[i])
            ind+=1
        while(heap):
            arr[ind]=heappop(heap)
            ind+=1
        