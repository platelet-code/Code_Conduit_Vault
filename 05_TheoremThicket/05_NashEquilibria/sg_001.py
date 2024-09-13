class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        positions.append([kx, ky])
        n = len(positions)

        @cache
        def knight_distance(start: Tuple[int, int], end: Tuple[int, int]) -> int:
            if start == end:
                return 0
                
            queue = deque([(start, 0)])
            visited = set([start])
            moves = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]
            
            while queue:
                (x, y), dist = queue.popleft()
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) == end:
                        return dist + 1
                    if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), dist + 1))
            
            return -1

        pairwise_dist = {}
        for i, x in enumerate(positions):
            for j, y in enumerate(positions):
                pairwise_dist[(i, j)] = knight_distance(tuple(x), tuple(y))

        @cache
        def dp(cur_idx: int, mask: int, maximize: bool = True) -> int:
            if mask == 0:
                return 0
            
            best_val = -float('inf') if maximize else float('inf')
            for next_idx in range(n):
                if (1 << next_idx) & mask:
                    dist = pairwise_dist[(cur_idx, next_idx)]
                    val = dp(next_idx, mask ^ (1 << next_idx), not maximize) + dist
                    if maximize:
                        best_val = max(best_val, val)
                    else:
                        best_val = min(best_val, val)
            return best_val

        return dp(n-1, (1 << (n-1)) - 1)
