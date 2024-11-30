from collections import defaultdict,deque
from typing import List
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        ind,outd = defaultdict(int),defaultdict(int)

        for i,j in pairs:
            graph[i].append(j)
            outd[i]+=1
            ind[j]+=1

        start = None
        stack = []
        for i in outd:
            if(outd[i]==ind[i]+1):
                start = i
                break
        # print(start)
        if(start==None):
            start = pairs[0][0]
        
        def topo(node):
            while(graph[node]):
                next = graph[node].popleft()
                topo(next)
            stack.append(node)
            
        topo(start)
        stack.reverse()

        res = []
        n = len(stack)
        for i in range(1,n):
            res.append([stack[i-1],stack[i]])

        return res

        

        