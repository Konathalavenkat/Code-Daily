class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res=[]
        items.sort(key=lambda x:(-x[1],x[0]))
        for i in queries:
            flag=True
            for j,k in items:
                if(j<=i):
                    flag=False
                    res.append(k)
                    break
            if(flag):
                res.append(0)
        return res