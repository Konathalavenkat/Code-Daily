from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        st = []
        for i in range(n):
            while(st and prices[st[-1]]>=prices[i]):
                prices[st.pop()]-=prices[i]
            st.append(i)
        return prices