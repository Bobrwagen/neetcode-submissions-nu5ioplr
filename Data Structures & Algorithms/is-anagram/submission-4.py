class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_map = defaultdict(int)
        for c in s:
            freq_map[c] += 1
        for c in t:
            if freq_map[c] == 0:
                return False
            freq_map[c] -= 1
        return True
