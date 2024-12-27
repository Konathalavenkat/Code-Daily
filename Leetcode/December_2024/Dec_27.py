class Solution:
    def maxScoreSightseeingPair(self, values) -> int:
        val = values[0]
        res = 0
        n = len(values)
        for i in range(1,n):
            res = max(res,val+values[i]-i)
            val = max(val,i+values[i])
        return res