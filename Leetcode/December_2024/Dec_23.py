# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root) -> int:
        def countswaps(arr):
            res=0
            copy=[i for i in arr]
            d={}
            copy.sort()
            for i in range(len(arr)):
                d[arr[i]]=i
            for i in range(len(arr)):
                if(arr[i]!=copy[i]):
                    res+=1
                    temp=arr[i]
                    arr[i],arr[d[copy[i]]]=arr[d[copy[i]]],arr[i]
                    d[temp]=d[copy[i]]
                    d[copy[i]]=i
            return res
            
        res=0
        a=[root]
        while(len(a)!=0):
            n=len(a)
            for i in range(n):
                temp=a.pop(0)
                if(temp.left):
                    a.append(temp.left)
                if(temp.right):
                    a.append(temp.right)
            res+=countswaps([i.val for i in a])
        return res