def main():
    n = int(input())
    energes = list(map(int, input().split()))
    
    def is_bule(x: int) -> bool:
        for energe in energes:
            if x < energe:
                x -= (energe - x)
            else:
                x += (x - energe)
            if x < 0:
                return False
        return True
            
    left, right = 1, 10 ** 5 + 10
    
    while left < right:
        pivot = (left + right) // 2
        if is_bule(pivot):
            right = pivot
        else:
            left = pivot + 1
    
    print(left)


if __name__ == "__main__":
    main()
