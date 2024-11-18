class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def reverse(self,arr,i,j):
        while(i<j):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        d=d%n
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
