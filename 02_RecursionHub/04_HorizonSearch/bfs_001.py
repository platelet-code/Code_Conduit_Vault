class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                stop_to_buses[x].append(i)
        
        if source not in stop_to_buses or target not in stop_to_buses:
            return 0 if source == target else -1
        
        dis = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft()
            dis_x = dis[x]
            for i in stop_to_buses[x]:
                if routes[i]:
                    for y in routes[i]:
                        if y not in dis:
                            dis[y] = dis_x + 1
                            q.append(y)
                    routes[i] = None
        
        return dis.get(target, -1)
