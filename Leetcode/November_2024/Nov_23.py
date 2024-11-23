class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def reverse(arr):
            l,r=0,len(arr)-1
            while(l<r):
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        m,n=len(box),len(box[0])
        rev=[['.']*n for i in range(m)]
        for i in range(m):
            prev=n-1
            for j in range(n-1,-1,-1):
                if(box[i][j]=='#'):
                    rev[i][prev]='#'
                    prev-=1
                elif(box[i][j]=='*'):
                    rev[i][j]='*'
                    prev=j-1
        res=[[rev[j][i] for j in range(m)] for i in range(n)]
        for i in res:
            reverse(i)
        return res