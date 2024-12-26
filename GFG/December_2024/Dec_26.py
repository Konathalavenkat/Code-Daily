class Solution:
    def twoSum(self, arr, target):
        # code here
        visited = set()
        for i in arr:
            if target - i in visited:
                return True
            visited.add(i)
        return False
