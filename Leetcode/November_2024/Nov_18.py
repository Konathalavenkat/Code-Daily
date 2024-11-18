from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        curr = 0
        n=len(code)
        res=[0]*n
        if(k>0):
            curr+=sum(code[1:k+1])
            for ind in range(n):
                res[ind]=curr
                curr+=code[(ind+k+1)%n]
                curr-=code[(ind+1)%n]
        elif(k<0):
            curr+=sum(code[k:])
            for ind in range(n):
                res[ind]=curr
                curr-=code[(ind+k)%n]
                curr+=code[ind]
        return res
