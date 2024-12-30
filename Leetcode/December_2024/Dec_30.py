class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp=[0]*(high+1)
        dp[0]=1
        mod = 10**9 + 7
        for i in range(1,high+1):
            for j in [zero,one]:
                if(i-j>=0):
                    dp[i]+=dp[i-j]
            dp[i]%=mod 
        return sum(dp[low:high+1])%mod