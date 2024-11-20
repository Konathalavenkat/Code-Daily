class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        ele1,ele2 = -1,-2
        cnt1,cnt2=0,0
        for i in arr:
            if(i==ele1):
                cnt1+=1
            elif(i==ele2):
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
                if(cnt1<0):
                    ele1 = i
                    cnt1 = 1
                elif(cnt2<0):
                    ele2 = i
                    cnt2 = 1
        # print(ele1,ele2)
        cnt1,cnt2=0,0
        for i in arr:
            if(i==ele1):
                cnt1+=1
            elif(i==ele2):
                cnt2+=1
        res=[]
        if(cnt1>len(arr)//3):
            res.append(ele1)
        if(cnt2>len(arr)//3):
            res.append(ele2)
        return sorted(res)