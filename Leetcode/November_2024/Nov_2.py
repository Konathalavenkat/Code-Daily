class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence=sentence.strip()
        if(sentence[-1]!=sentence[0]):
            return False
        words=sentence.split()
        prev=words[0]
        for i in words[1:]:
            if(i[0]!=prev[-1]):
                return False
            prev=i
        return True