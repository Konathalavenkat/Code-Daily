from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        keys = sorted(list(c.keys()))
        n = len(keys)
        res = []
        repeat = 0
        for i in range(len(s)):
            lar,seclar = keys[-1] if n>0 else None,keys[-2] if n>1 else None
            if(not lar):
                break
            if(repeat>=repeatLimit):
                repeat = 0
                if(not seclar):
                    break
                res.append(seclar)
                c[seclar]-=1
                if(c[seclar]==0):
                    repeat = 0
                    keys.pop(n-2)
                    n-=1
            else:
                temp = min(c[lar],repeatLimit)
                res.append(lar*temp)
                repeat += temp
                c[lar]-= temp
                if(c[lar]==0):
                    repeat = 0
                    keys.pop()
                    n-=1
            # print(lar,seclar,repeat,''.join(res))
        return ''.join(res)