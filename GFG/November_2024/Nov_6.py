class Solution:
    def treePathSum(self,root):
        # Code here
        res=[0]
        def util(root,curr):
            if(root):
                curr=curr*10+root.data
                if(not root.left and not root.right):
                    res[0]+=curr
                util(root.left,curr)
                util(root.right,curr)
        util(root,0)
        return res[0]