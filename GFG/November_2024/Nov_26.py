def circularSubarraySum(arr):
    def kadane(arr):
        prefix = 0
        res = -1e9
        for i in arr:
            prefix += i
            res = max(res,prefix)
            if(prefix<0):
                prefix = 0
        return res
    x = kadane(arr)
    s = sum(arr)
    arr = list(map(lambda x:-x,arr))
    y = s+kadane(arr)
    if(y>0):
        return max(x,y)
    return x