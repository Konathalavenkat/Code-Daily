class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        zero , ones = 0,s.count('1')
        for i in s[:-1]:
            if i == '0':
                zero+=1
            else:
                ones-=1
            res=max(res,zero+ones)
        return res