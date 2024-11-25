from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_cnt = 0
        min_neg = -1e9
        total=0

        for i in matrix:
            for j in i:
                total += abs(j)
                if(j<=0):
                    neg_cnt+=1
                if(abs(j)<abs(min_neg)):
                    min_neg = -abs(j)
        # print(total,min_neg)
        return total if neg_cnt%2==0 else total + 2*min_neg