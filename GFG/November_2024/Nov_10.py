class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        res=[]
        m,n=len(a),len(b)
        ind1,ind2=0,0
        while(ind1<m and ind2<n):
            if(a[ind1]==b[ind2]):
                res.append(a[ind1])
                ind1+=1
                ind2+=1
            elif(a[ind1]<b[ind2]):
                res.append(a[ind1])
                ind1+=1
            else:
                res.append(b[ind2])
                ind2+=1
        for i in range(ind1,m):
            res.append(a[i])
        for i in range(ind2,n):
            res.append(b[i])
        return res