class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        return True if len(s1)==len(s2) and s1 in s2+s2 else False