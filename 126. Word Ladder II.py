class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        # bfs build graph + dfs memo
        graph = defaultdict(set)
        queue = Deque([beginWord])
        step = 0
        min_step = -1
        visited = set()
        while len(queue):
            size = len(queue)
            step += 1
            for _ in range(size):
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                for i in range(len(cur)):
                    c = cur[i]
                    for j in range(26):
                        n_c = chr(ord('a') + j)
                        if n_c == c:
                            continue
                        n_s = cur[0:i] + n_c + cur[i+1:]
                        if n_s in word_set:
                            graph[n_s].add(cur)
                            graph[cur].add(n_s)
                            queue.append(n_s)
                        if n_s == endWord and min_step == -1:
                            min_step = step
        @lru_cache(None)
        def dfs(cur, step):
            nonlocal graph
            if step > min_step:
                return []
            if cur == endWord:
                return [[endWord]]
            res = []
            for nxt in graph[cur]:
                tmp = dfs(nxt,step+1)
                res += [[cur] + x for x in tmp]
            # print(res)
            return res
        return dfs(beginWord, 0)
        
        