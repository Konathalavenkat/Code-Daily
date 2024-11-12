class Solution:
    def canAttend(self,arr):
        # Your Code Here
        arr.sort(key=lambda x:(x[1],x[0]))
        prev=-1e9
        for i,j in arr:
            if(i<prev):
                return False
            prev=j
        return True