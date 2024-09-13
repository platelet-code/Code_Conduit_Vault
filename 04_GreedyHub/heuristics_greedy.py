def huffman_tree_cost(numbers: List[int]) -> int:
    import heapq
    heapq.heapify(numbers)
    total_cost = 0
    while len(numbers) > 1:
        first_min = heapq.heappop(numbers)
        second_min = heapq.heappop(numbers)
        total_cost += first_min + second_min
        heapq.heappush(numbers, first_min + second_min)
    return total_cost


def minimize_total_wait(times: List[int]) -> int:
    times.sort()
    total_waiting_time = 0
    current_wait = 0
    for time in times:
        total_waiting_time += current_wait
        current_wait += time
    return total_waiting_time


def optimal_warehouse_location(shops: List[int]) -> int:
    shops.sort()
    total_distance = 0
    for i in range(len(shops)):
        total_distance += shops[i] - shops[i >> 1]
    return total_distance


def minimize_stack_risk(items: List[Tuple[int, int]]) -> int:
    items = [(weight + strength, weight) for weight, strength in items]
    items.sort()

    max_risk = -float('inf')
    total_weight = 0

    for total, weight in items:
        strength = total - weight
        risk = total_weight - strength
        max_risk = max(max_risk, risk)
        total_weight += weight
        
    return max_risk
