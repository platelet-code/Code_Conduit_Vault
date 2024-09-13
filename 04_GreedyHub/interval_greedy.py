def interval_merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
    ans = []
    for p in intervals:
        if ans and p[0] <= ans[-1][1]:  # 可以合并
            ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
        else:  # 不相交，无法合并
            ans.append(p)  # 新的合并区间
    return ans


def interval_select(intervals: List[Tuple[int, int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    points = []
    
    last_covered_end = float('-inf')
    
    for start, end in intervals:
        if start > last_covered_end:
            last_covered_end = end
            points.append(last_covered_end)
    
    return len(points)


def interval_group(intervals: List[Tuple[int, int]]) -> int:
    intervals.sort()
    import heapq
    heap = []
    for interval in intervals:
        if heap and heap[0] < interval[0]:
            heapq.heapreplace(heap, interval[1])
        else:
            heapq.heappush(heap, interval[1])
    return len(heap)


def interval_coverage(start: int, end: int, intervals: List[Tuple[int, int]]) -> int:
    if start == end:
        return 1 if any(a <= start <= b for a, b in intervals) else -1
    
    intervals = [x for x in intervals if x[0] <= end and x[1] >= start]
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    count = 0
    current_end = start
    
    i = 0
    while current_end < end:
        max_end = current_end
        while i < len(intervals) and intervals[i][0] <= current_end:
            max_end = max(max_end, intervals[i][1])
            i += 1
        if max_end == current_end:
            return -1
        current_end = max_end
        count += 1
        
    return count
