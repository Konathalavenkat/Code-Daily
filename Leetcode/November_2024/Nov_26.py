from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        outdegree = [0]*n
        for i,j in edges:
            outdegree[j]+=1
        res = []
        for i in range(n):
            if(outdegree[i]==0):
                res.append(i)
        if(len(res)!=1):
            return -1
        return res[0]