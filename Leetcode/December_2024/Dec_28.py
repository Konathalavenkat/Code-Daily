from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        subsums = []
        curr = sum(nums[:k])
        subsums.append(curr)
        n = len(nums)
        for i in range(k,n):
            curr += nums[i]-nums[i-k]
            subsums.append(curr)
        dp = [[[-1e9,-1,-1] for i in range(3)] for _ in range(n-k+1)]
        for i in range(n-k+1):
            dp[i][0]=[subsums[i],i,i]
        for i in range(1,n-k+1):
            for j in range(2,-1,-1):
                if(j!=2 and dp[i-1][j][0]>=dp[i][j][0]):
                    dp[i][j]=dp[i-1][j][:]
                if(j-1>=0 and i-k>=0):
                    if(dp[i-k][j-1][0]+dp[i][0][0]>dp[i][j][0]):
                        dp[i][j]=[dp[i-k][j-1][0]+dp[i][0][0],i-k,i]
        # for i in dp:
        #     print(i)
        max,ind = -1e9,-1
        for i in range(n-k+1):
            if(dp[i][2][0]>max):
                max = dp[i][2][0]
                ind = i
        second = dp[ind][2][1]
        first = dp[second][1][1]
        return [dp[first][0][2],dp[second][1][2],ind]