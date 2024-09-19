class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] = max(self.tree[idx], val)
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res = max(res, self.tree[idx])
            idx -= idx & -idx
        return res


class Solution:
    def maxPathLength(self, nums: List[List[int]], k: int) -> int:
        kx, ky = nums[k]
        nums.sort(key=lambda p: (p[0], -p[1]))
        nums_rev = [[-x, -y] for x, y in nums]
        nums_rev.sort(key=lambda p: (p[0], -p[1]))
        
        def getLen(points, target_x, target_y):
            ys = [y for x, y in points]
            sorted_ys = sorted(set(ys))
            y_idx = {y: i+1 for i, y in enumerate(sorted_ys)}
            bit = FenwickTree(len(sorted_ys))
            for x, y in points:
                idx = y_idx[y]
                cur_len = bit.query(idx - 1) + 1
                if x == target_x and y == target_y:
                    return cur_len
                bit.update(idx, cur_len)
            return 0
        
        len_forward = getLen(nums, kx, ky)
        len_backward = getLen(nums_rev, -kx, -ky)
        return len_forward + len_backward - 1
