from typing import List
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        m = max(nums) 
        cnt = [0] * (m + 1)
        for num in nums:
            cnt[max(num - k, 0)] += 1 
            if num + k + 1 <= m:
                cnt[num + k + 1] -= 1 

        res = 0
        s = 0 

        for val in cnt:
            s += val
            res = max(res, s)

        return res