def reverse(arr):
    l,r=0,len(arr)-1
    while(l<r):
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
def rotate(matrix): 
    #code here
    m=101
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j]=((matrix[j][i]%m)*m+matrix[i][j])
    for i in range(n):
        reverse(matrix[i])
        for j in range(n):
            matrix[i][j]//=m
    return matrix