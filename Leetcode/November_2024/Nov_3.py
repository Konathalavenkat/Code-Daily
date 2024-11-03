class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m,n=len(s),len(goal)
        if(m!=n):
            return False
        return goal in s+s
    