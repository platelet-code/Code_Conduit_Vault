class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = 0
        s = 0
        left = 0
        q = deque()

        for right, (charge, cost) in enumerate(zip(chargeTimes, runningCosts)):
            # 入队
            while q and charge >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right)
            s += cost
            
            # 出队
            while q and chargeTimes[q[0]] + (right - left + 1) * s > budget:
                if q[0] == left:
                    q.popleft()
                s -= runningCosts[left]
                left += 1
            
            # 更新答案
            ans = max(ans, right - left + 1)
        
        return ans
