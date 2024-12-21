from typing import List
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        res = [0]
        def dfs(root,parent):
            sum = values[root]
            for i in adj[root]:
                if i!=parent:
                    sum += dfs(i,root)
            if(sum%k==0):
                res[0]+=1
            return sum
        dfs(0,None)
        return res[0]