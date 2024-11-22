class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def makestr(arr):
            res  = []
            inc = 0
            if(arr[0]==1):
                inc = 1
            for i in arr:
                res.append(str((i+inc)%2))
            return ''.join(res)
        mp = defaultdict(int)
        for i in matrix:
            mp[makestr(i)]+=1
        return max(mp.values())