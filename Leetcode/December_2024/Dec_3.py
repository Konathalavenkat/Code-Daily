from collections import deque
from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        spaces = deque(spaces)
        for i,val in enumerate(s):
            if(spaces and i==spaces[0]):
                res.append(' ')
                spaces.popleft()
            res.append(val)
        return ''.join(res)