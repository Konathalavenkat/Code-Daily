from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0]*(n+1)
        curr_pref = 0
        vowels = set('aeiou')
        for i,val in enumerate(words):
            if val[0] in vowels and val[-1] in vowels:
                curr_pref += 1
            prefix[i]=curr_pref
        res = []
        for i,j in queries:
            res.append(prefix[j]-prefix[i-1])
        return res
    