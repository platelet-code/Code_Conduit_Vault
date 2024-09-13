def lengthOfLIS(arr: List[int]) -> int:
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lengthOfLIS(nums: List[int]) -> int:
    from bisect import bisect_left
    tails = []
    for num in nums:
        idx = bisect_left(tails, num)  # 使用二分查找确定插入位置
        if idx == len(tails):          # 如果是新的更长序列，添加到末尾
            tails.append(num)
        else:
            tails[idx] = num           # 否则更新存在的位置   
    return len(tails)                  # 返回最长上升子序列的长度


def lengthOfLIS(nums: List[int]) -> int:
    from functools import lru_cache
    @lru_cache(None)
    def lis_ending_at(index: int) -> int:
        max_len = 1
        for previous in range(index):
            if nums[previous] < nums[index]:
                max_len = max(max_len, lis_ending_at(previous) + 1)
        return max_len
    return max(lis_ending_at(i) for i in range(len(nums)))
