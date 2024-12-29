class Solution:
    def intersectionWithDuplicates(self, a, b):
        return sorted(list(set(a).intersection(set(b))))