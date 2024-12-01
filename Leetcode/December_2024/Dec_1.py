from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
       n = len(arr)
       d=set()
       for i in arr:
        if(i/2 in d or i*2 in d):
            return True
        d.add(i)
       return False