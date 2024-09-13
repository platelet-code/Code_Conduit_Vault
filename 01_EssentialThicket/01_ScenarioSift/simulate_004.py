def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    first_ant = abs(nums[0])
    left_ant = right_ant = 0
    
    for i in range(1, n):
        current_ant = abs(nums[i])
        if current_ant > first_ant:
            left_ant += nums[i] < 0
        elif current_ant < first_ant:
            right_ant += nums[i] > 0
    
    if (nums[0] > 0 and left_ant > 0) or (nums[0] < 0 and right_ant > 0):
        print(left_ant + right_ant + 1)
    else:
        print(1)


if __name__ == "__main__":
    main()
