class Solution:
    def makeFancyString(self, s: str) -> str:
        res=[]
        prev=''
        cnt=0
        for i in s:
            if(i==prev):
                cnt+=1
            else:
                res.append(prev*(min(cnt,2)))
                cnt=1
                prev=i
        res.append(prev*(min(cnt,2)))
        return ''.join(res)