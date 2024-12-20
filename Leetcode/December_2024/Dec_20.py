from collections import deque
class Solution:
    def reverseOddLevels(self, root):
        q=deque()
        q.append(root)
        rev=False
        while q:
            qz=len(q)
            arr=[]
            for i in range(qz):
                Node=q.popleft()
                if Node.left: q.append(Node.left)
                if Node.right: q.append(Node.right)
                if rev:
                    arr.append(Node)
                    if i>=qz/2:
                        arr[i].val, arr[qz-1-i].val=arr[qz-1-i].val, arr[i].val
            rev=not rev
        return root