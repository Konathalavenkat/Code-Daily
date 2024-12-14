class Solution:
    def search(self,arr,key):
        n = len(arr)
        l,r = 0,n-1
        while(l<=r):
            mid = (l+r)//2
            if(arr[mid]>key):
                if(arr[mid]>=arr[l] and arr[l]>key):
                    l = mid + 1
                else:
                    r = mid-1
            elif(arr[mid]<key):
                if(arr[mid]<=arr[r] and arr[r]<key):
                    r = mid-1
                else:
                    l = mid + 1
            else:
                return mid
        return -1
