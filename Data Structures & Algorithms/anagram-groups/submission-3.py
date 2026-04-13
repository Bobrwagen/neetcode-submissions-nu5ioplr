class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            chars = [0] * 26
            for c in w:
                ind = ord(c) - ord('a')
                chars[ind] += 1
            chars = tuple(chars)
            res[chars].append(w)
        print(res)
        return list(res.values())
