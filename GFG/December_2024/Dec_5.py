class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        left,mid,right=0,0,len(arr)-1
        while(mid<=right):
            if(arr[mid]==0):
                arr[mid]=arr[left]
                arr[left]=0
                mid+=1
                left+=1
            elif(arr[mid]==2):
                arr[mid]=arr[right]
                arr[right]=2
                right-=1
            else:
                mid+=1
        return arr