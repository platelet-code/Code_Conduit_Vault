class Node:
    __slots = 'son', 'fail', 'len'

    def __init__(self, len=0):
        self.son = [None] * 26
        self.fail = None
        self.len = len

class AhoCorasick:
    def __init__(self):
        self.root = Node()
    
    def put(self, s: str) -> None:
        cur = self.root
        for b in s:
            b = ord(b) - ord('a')
            if cur.son[b] is None:
                cur.son[b] = Node(cur.len + 1)
            cur = cur.son[b]
    
    def build_fail(self) -> None:
        self.root.fail = self.root
        q = deque()
        for i, son in enumerate(self.root.son):
            if son is None:
                self.root.son[i] = self.root
            else:
                son.fail = self.root
                q.append(son)
        
        while q:
            cur = q.popleft()
            for i, son in enumerate(cur.son):
                if son is None:
                    cur.son[i] = cur.fail.son[i]
                    continue
                son.fail = cur.fail.son[i]
                q.append(son)


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        ac = AhoCorasick()
        for w in words:
            ac.put(w)
        ac.build_fail()

        n = len(target)
        f = [0] * (n + 1)
        cur = root = ac.root
        for i, c in enumerate(target, 1):
            cur = cur.son[ord(c) - ord('a')]
            if cur is root:
                return -1
            f[i] = f[i - cur.len] + 1
        
        return f[n]
