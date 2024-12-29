from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n,m= len(target),len(words[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        char = [[0]*26 for _ in range(m)]
        mod = 1000000007
        def getind(ch):
            return ord(ch)-ord("a")
        for i in words:
            for j in range(m):
                char[j][getind(i[j])]+=1
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = (dp[i-1][j] + char[i-1][getind(target[j-1])]*dp[i-1][j-1])%mod
        return dp[m][n]