class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        arr = [0]*26
        for i in s:
            arr[ord(i)-97]+=1
        for i in s:
            if(arr[ord(i)-97]==1):
                return i
        return -1
            
    