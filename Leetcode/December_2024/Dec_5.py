from collections import deque
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        lst=deque()
        rst=[]
        for i,val in enumerate(start):
            if(val in ['L','R']):
                lst.append([i,val])
        for i,val in enumerate(target):
            while(lst and lst[0][0]<=i and lst[0][1]=='R'):
                rst.append(lst.popleft())
            if(lst and lst[0][0]<i and lst[0][1]=='L'):
                return False        
            if(val == 'L'):
                if(rst):
                    # print("At Rst")
                    return False
                if(lst and lst[0][1]=='L'):
                    lst.popleft()
                    continue
                else:
                    return False
            elif(val== 'R'):
                if(rst and rst[-1][1]):
                    rst.pop()
                else:
                    return False
        return not lst and not rst
            


