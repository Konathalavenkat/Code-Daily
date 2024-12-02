class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split()
        n=len(searchWord)
        for i,val in enumerate(arr):
            if(len(val)>=n and val[:n]==searchWord):
                return i+1
        return -1