from typing import Optional, List, TreeNode
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        q = deque()
        if(not root):
            return res
        q.append(root)
        while(q):
            n = len(q)
            curr = -1e15
            for i in range(n):
                top = q.popleft()
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                curr = max(curr,top.val)
            res.append(curr)
        return res