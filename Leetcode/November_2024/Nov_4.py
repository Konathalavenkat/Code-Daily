class Solution:
    def compressedString(self, word: str) -> str:
        res=[]
        cnt=0
        prev=word[0]
        for i in word:
            if(i==prev):
                cnt+=1
                if(cnt==9):
                    res.append('9')
                    res.append(prev)
                    cnt=0
            else:
                if(cnt!=0):
                    res.append(str(cnt))
                    res.append(prev)
                prev=i
                cnt=1
        if(cnt!=0):
            res.append(str(cnt))
            res.append(prev)
        return ''.join(res)