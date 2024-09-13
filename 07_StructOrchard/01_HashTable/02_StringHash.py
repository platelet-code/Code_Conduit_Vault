class StringHash:
    def __init__(self, s: str):
        self.s = s
        self.BASE = 13331
        self.MOD = 1000000007
        self.n = len(s)
        self.prefix_hash = [0] * (self.n + 1)
        self.power = [1] * (self.n + 1)
        self._precompute()

    def _precompute(self):
        for i in range(1, self.n + 1):
            self.power[i] = (self.power[i - 1] * self.BASE) % self.MOD
            self.prefix_hash[i] = (self.prefix_hash[i - 1] * self.BASE + ord(self.s[i - 1])) % self.MOD

    def get_substring_hash(self, l: int, r: int) -> int:
        return (self.prefix_hash[r] - self.prefix_hash[l - 1] * self.power[r - l + 1] % self.MOD + self.MOD) % self.MOD

    def compare_substrings(self, l1: int, r1: int, l2: int, r2: int) -> bool:
        return self.get_substring_hash(l1, r1) == self.get_substring_hash(l2, r2)
