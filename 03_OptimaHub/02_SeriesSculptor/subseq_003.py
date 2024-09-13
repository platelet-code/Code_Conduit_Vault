def lengthOfLICS(nums1: list, nums2: list) -> int:
    n, m = len(nums1), len(nums2)
    f = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        maxv = 0
        for j in range(1, m + 1):
            f[i][j] = f[i - 1][j]
            if nums1[i - 1] == nums2[j - 1]:
                f[i][j] = max(f[i][j], maxv + 1)

            if nums2[j - 1] < nums1[i - 1]:
                maxv = max(maxv, f[i - 1][j])

    result = max(f[n][j] for j in range(m + 1))
    return result
