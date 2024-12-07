class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        res=[0]
        def mergesort(arr,l,r):
            if(l<r):
                mid = (l+r)//2
                mergesort(arr,l,mid)
                mergesort(arr,mid+1,r)
                merge(arr,l,mid,r)
        def merge(arr,l,mid,r):
            i,j = l,mid+1
            # print(arr[l:mid+1],arr[mid+1:r+1])
            temp=[]
            while(i<=mid and j<=r):
                if(arr[i]<=arr[j]):
                    temp.append(arr[i])
                    i+=1
                else:
                    res[0]+=mid-i+1
                    temp.append(arr[j])
                    j+=1
            while(i<=mid):
                temp.append(arr[i])
                i+=1
            while(j<=r):
                temp.append(arr[j])
                j+=1
            for k in range(l,r+1):
                arr[k]=temp[k-l]
            # print(res)
        mergesort(arr,0,len(arr)-1)
        return res[0]