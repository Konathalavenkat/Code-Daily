class Solution:
    def myAtoi(self, s):
        # Code here
        s=s.strip()
        if s:
            sign=1
            lb=-2**31
            rb=2**31-1
            if s[0] in ['+','-']:
                sign = int(s[0]+'1')
                s=s[1:]
            num=0
            for i in s:
                if(i.isdigit()):
                    num=num*10+int(i)
                else:
                    return sign*num
                if(not lb<=sign*num<=rb):
                    return rb if sign>0 else lb
                # print(num)
            return sign*num
        return 0