class Node:
    __slots__ = 'son', 'fail', 'last', 'len', 'cost'

    def __init__(self):
        self.son = [None] * 26
        self.fail = None 
        self.last = None
        self.len = 0
        self.cost = inf


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def put(self, s: str, cost: int) -> None:
        cur = self.root
        for b in s:
            b = ord(b) - ord('a')
            if cur.son[b] is None:
                cur.son[b] = Node()
            cur = cur.son[b]
        cur.len = len(s)
        cur.cost = min(cur.cost, cost)

    def build_fail(self) -> None:
        self.root.fail = self.root.last = self.root
        q = deque()
        for i, son in enumerate(self.root.son):
            if son is None:
                self.root.son[i] = self.root
            else:
                son.fail = son.last = self.root
                q.append(son)

        while q:
            cur = q.popleft()
            for i, son in enumerate(cur.son):
                if son is None:
                    cur.son[i] = cur.fail.son[i]
                    continue
                son.fail = cur.fail.son[i]
                son.last = son.fail if son.fail.len else son.fail.last
                q.append(son)


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        ac = AhoCorasick()
        for w, c in zip(words, costs):
            ac.put(w, c)
        ac.build_fail()

        n = len(target)
        f = [0] + [inf] * n
        cur = root = ac.root
        for i in range(1, n + 1):
            cur = cur.son[ord(target[i - 1]) - ord('a')]
            if cur.len:
                f[i] = min(f[i], f[i - cur.len] + cur.cost)
            match_node = cur.last
            while match_node != root:
                tmp = f[i - match_node.len] + match_node.cost
                if tmp < f[i]:
                    f[i] = tmp
                match_node = match_node.last
        return -1 if f[n] == inf else f[n]
