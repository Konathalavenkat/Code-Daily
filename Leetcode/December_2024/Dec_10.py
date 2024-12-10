from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        d=defaultdict(lambda:defaultdict(int))
        prev = '$'
        cnt = 0
        for i in s:
            if(i!=prev):
                for j in range(1,cnt+1):
                    d[prev][j]+=cnt-j+1
                prev = i
                cnt = 1
            else:
                cnt+=1
        for j in range(1,cnt+1):
            d[prev][j]+=cnt-j+1
        # print(d)
        res = -1
        for i in d:
            # print(i)
            for j in d[i]:
                # print(j,d[i][j])
                if(d[i][j]>=3):
                    res=max(res,j)
        return res