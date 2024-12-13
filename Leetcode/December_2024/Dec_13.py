class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap=[[val,i] for i,val in enumerate(nums)]
        heap.sort()
        score = 0
        marked = set()
        for least,ind in heap:
            if(ind not in marked):
                score+=least
                marked.add(ind)
                marked.add(ind+1)
                marked.add(ind-1)
        return score