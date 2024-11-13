def intersetPoint(head1,head2):
    #code here
    l1,l2=head1,head2
    while(l1!=l2):
        l1 = l1.next if l1 else head2
        l2= l2.next if l2 else head1
    return l1.data if l1 else -1