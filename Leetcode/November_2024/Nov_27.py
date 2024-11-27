from typing import List
from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(n)]
        for i in range(n-1):
            adj[i].add(i+1)
        res = []
        for u,v in queries:
            adj[u].add(v)
            q = deque()
            q.append((0,0))
            visited = set()
            visited.add(0)
            while(q):
                top,distance = q.popleft()
                visited.add(top)
                if(top == n-1):
                    res.append(distance)
                    break
                for i in adj[top]:
                    if(i not in visited):
                        q.append((i,distance+1))    
        return res
