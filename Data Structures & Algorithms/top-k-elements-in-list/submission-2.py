class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        buckets = [[]]
        highest = 0
        for num in nums:
            frequency = 1 + frequency_map.get(num, 0)
            if frequency > highest:
                buckets.append([num])
            else:
                buckets[frequency].append(num)
            # remove previous
            if frequency > 1:
                buckets[frequency-1].remove(num)
            # update highest
            highest = max(frequency, highest)
            # update frequency map
            frequency_map[num] = 1 + frequency_map.get(num, 0)
        res = []
        while k > 0:
            while buckets[-1]:
                if k == 0:
                    break
                res.insert(0, buckets[-1][-1])
                buckets[-1].pop(-1)
                k -= 1
            buckets.pop(-1)
        return res



        