class NumArray:
    def __init__(self, nums: List[int]):
        # s = list(accumulate(nums, initial=0))
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2 + 1][c2 + 1] - self.s[r2 + 1][c1] - self.s[r1][c2 + 1] + self.s[r1][c1]


class DiffArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.diff = [0] * (self.n + 1)
        self.diff[0] = nums[0]
        for i in range(1, self.n):
            self.diff[i] = nums[i] - nums[i - 1]

    def update(self, from_: int, to: int, val: int) -> None:
        self.diff[from_] += val
        if to + 1 < self.n:
            self.diff[to + 1] -= val

    def reconstruct(self) -> List[int]:
        return list(itertools.accumulate(self.diff[:self.n]))


class DiffMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0]) if self.n > 0 else 0
        self.diff = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        self.populate(matrix)

    def populate(self, matrix: List[List[int]]) -> None:
        for r in range(self.n):
            for c in range(self.m):
                self.update(r, c, r, c, matrix[r][c])

    def update(self, r1: int, c1: int, r2: int, c2: int, value: int) -> None:
        self.diff[r1][c1] += value
        if c2 + 1 < self.m:
            self.diff[r1][c2 + 1] -= value
        if r2 + 1 < self.n:
            self.diff[r2 + 1][c1] -= value
        if r2 + 1 < self.n and c2 + 1 < self.m:
            self.diff[r2 + 1][c2 + 1] += value

    def reconstruct(self):
        final = [[0] * self.m for _ in range(self.n)]
        for r in range(self.n):
            for c in range(self.m):
                if r > 0:
                    self.diff[r][c] += self.diff[r - 1][c]
                if c > 0:
                    self.diff[r][c] += self.diff[r][c - 1]
                if r > 0 and c > 0:
                    self.diff[r][c] -= self.diff[r - 1][c - 1]
                final[r][c] = self.diff[r][c]
        return final
