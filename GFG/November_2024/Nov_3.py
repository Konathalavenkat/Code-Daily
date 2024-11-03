class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        fast=head
        while(fast and fast.next):
            fast=fast.next.next
        return not fast