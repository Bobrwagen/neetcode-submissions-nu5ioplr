class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        high = -2_000_000_000
        low = 2_000_000_000
        for n in nums:
            dic[n] = 1 
            if n > high:
                high = n
            if n < low:
                low = n
        currCounter = 0
        res = 0
        print(dic)
        for i in range(low,high+1):
            if dic.get(i):
                currCounter+= 1
            else:
                res = max(res,currCounter)
                currCounter = 0
        res = max(res,currCounter)    
        return res

        