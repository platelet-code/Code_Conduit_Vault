def zero_one_knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(capacity + 1):
            if j >= weights[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-weights[i]] + values[i])
            else:
                dp[i+1][j] = dp[i][j]
                
    return dp[n][capacity]


def zero_one_knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(2)]

    for i in range(n):
        for j in range(capacity + 1):
            dp[(i+1) & 1][j] = dp[i & 1][j]
            if j >= weights[i]:
                dp[(i+1) & 1][j] = max(dp[i & 1][j], dp[i & 1][j-weights[i]] + values[i])

    return dp[n & 1][capacity]


def zero_one_knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for w, v in zip(weights, values):
        for j in range(capacity, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    
    return max(dp)


def complete_knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(capacity + 1):
            dp[i+1][j] = dp[i][j]
            if j >= weights[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i+1][j-weights[i]] + values[i])

    return dp[n][capacity]


def complete_knapsack(capacity: int, weights: List[int], values: List[int]) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j-weights[i]] + values[i])

    return dp[capacity]


def multiple_knapsack(capacity: int, weights: List[int], values: List[int], counts: List[int]) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(capacity + 1):
            dp[i+1][j] = dp[i][j]
            max_k = min(counts[i], j // weights[i])
            for k in range(1, max_k + 1):
                dp[i+1][j] = max(dp[i+1][j], dp[i][j - k * weights[i]] + k * values[i])

    return dp[n][capacity]


def multiple_knapsack(capacity: int, weights: List[int], values: List[int], counts: List[int]) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(1, counts[i] + 1):
            for k in range(capacity, weights[i] - 1, -1):
                dp[k] = max(dp[k], dp[k - weights[i]] + values[i])

    return max(dp)


def multiple_knapsack(capacity: int, weights: List[int], values: List[int], counts: List[int]) -> int:
    n = len(weights)
    items = []

    for i in range(n):
        k = 1
        while k <= counts[i]:
            items.append((weights[i] * k, values[i] * k))
            counts[i] -= k
            k *= 2
        if counts[i] > 0:
            items.append((weights[i] * counts[i], values[i] * counts[i]))

    dp = [0] * (capacity + 1)

    for weight, value in items:
        for j in range(capacity, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[capacity]


def multiple_knapsack(capacity: int, weights: List[int], values: List[int], counts: List[int]) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for mod in range(weights[i]):
            queue = []
            max_range = (capacity - mod) // weights[i]
            for k in range(max_range + 1):
                val = dp[k * weights[i] + mod] - k * values[i]
                
                while queue and queue[-1][1] <= val:
                    queue.pop()
                queue.append((k, val))
                
                if queue[0][0] < k - counts[i]:
                    queue.pop(0)
                
                dp[k * weights[i] + mod] = queue[0][1] + k * values[i]

    return dp[capacity]


def group_knapsack(max_capacity: int, groups_items: List[List[Tuple[int, int]]]) -> int:
    dp = [0] * (max_capacity + 1)
    
    for items in groups_items:
        for cur_capacity in range(max_capacity, -1, -1):
            for weight, value in items:
                if weight <= cur_capacity:
                    dp[cur_capacity] = max(dp[cur_capacity], dp[cur_capacity - weight] + value)

    return dp[max_capacity]
