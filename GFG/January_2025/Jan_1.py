from collections import defaultdict
class Solution:
    def anagrams(self, arr):
        d=defaultdict(list)
        for i in arr:
            d[''.join(sorted(i))].append(i)
        res = []
        for i in d:
            res.append(d[i])
        return res
