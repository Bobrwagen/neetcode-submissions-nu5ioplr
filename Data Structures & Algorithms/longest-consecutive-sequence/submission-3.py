class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            visited.add(num)
        res = 0
        for num in visited:
            if num - 1 not in visited:
                seq = 1
                temp = num
                while temp + 1 in visited:
                    temp += 1
                    seq += 1
                res = max(res, seq)
        
        return res