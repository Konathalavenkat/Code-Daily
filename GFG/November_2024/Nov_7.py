class Solution:
    # Function to determine if array arr can be split into three equal sum sets.
    def findSplit(self, arr):
        s=sum(arr)
        # print(s,s%3,s//3)
        if(s%3!=0):
            return [-1,-1]
        req=s//3
        cnt=0
        pref=0
        for i in arr:
            pref+=i
            # print(pref)
            if(pref==req):
                cnt+=1
                pref=0
        # print(cnt)
        if(cnt>=3):
            return True
        return [-1,-1]