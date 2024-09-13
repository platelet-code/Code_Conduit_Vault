def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low >= high:
        return
    
    i, j = low, high
    pivot = arr[random.randint(low, high)]
    
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, low, j)
    quick_sort(arr, j + 1, high)


def merge_sort(nums: List[int], low: int, high: int) -> None:
    if low == high:
        return

    mid = (low + high) // 2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid + 1, high)

    merged = []
    i, j = low, mid + 1
    for _ in range(low, high + 1):
        if j > high or (i <= mid and nums[i] <= nums[j]):
            merged.append(nums[i])
            i += 1
        else:
            merged.append(nums[j])
            j += 1
            
    nums[low:high+1] = merged
