class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        neighbours = defaultdict(list)
        queue = [beginWord]
        level = 0
        while queue:
            new_queue = []
            level += 1
            for w in queue:
                if w in visited:
                    continue
                else:
                    visited.add(w)
                for i in range(len(w)):
                    pref = w[:i]
                    suff = w[i+1:]
                    print(w, pref, suff)
                    for n in wordList:
                        if n.startswith(pref) and n.endswith(suff):
                            if n == endWord:
                                return level + 1
                            else:
                                neighbours[w].append(n)
                new_queue += neighbours[w]
            queue = new_queue
            print(queue)
        return 0
                    

        