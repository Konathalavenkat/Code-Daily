class Solution:
    def isLengthEven(self, head):
        fast=head
        while(fast and fast.next):
            fast=fast.next.next
        return not fast