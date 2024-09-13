def main():
    N, R = map(int, input().split())
    R = min(R, 5001)
    W = H = R
    MAX_N = 5010
    
    s = [[0] * MAX_N for _ in range(MAX_N)]
    for _ in range(N):
        x, y, z = map(int, input().split())
        x += 1
        y += 1
        s[x][y] += z
        W = max(x, W)
        H = max(y, H)
    
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
    
    ret = 0
    for i in range(R, W + 1):
        for j in range(R, H + 1):
            sum_region = s[i][j] - s[i - R][j] - s[i][j - R] + s[i - R][j - R]
            ret = max(ret, sum_region)
    
    print(ret)


if __name__ == "__main__":
    main()
