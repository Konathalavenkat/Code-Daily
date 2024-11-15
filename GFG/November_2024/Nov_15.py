class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest , second = -1,-1
        for i in arr:
            if(i>largest):
                second = largest
                largest = i
            elif(i!=largest):
                second = max(second,i)
        return second