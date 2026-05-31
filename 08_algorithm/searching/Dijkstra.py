import heapq

def path_finder(area: str) -> int:
    grid = [row for row in area.split("\n")]
    grid_cost = [[float("inf") for _ in range(len(grid))] for _ in range(len(grid))]
    grid_cost[0][0] = 0
    
    queue = [(grid_cost[0][0], 0, 0)]
    
    while queue:
        cost, x, y = heapq.heappop(queue)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for direction in directions:
            x_neighbor, y_neighbor = x + direction[0], y + direction[1]
            if not 0 <= x_neighbor < len(grid) or not 0 <= y_neighbor < len(grid):
                continue
            cost_new = cost + abs(int(grid[x][y]) - int(grid[x_neighbor][y_neighbor]))
            if cost_new < grid_cost[x_neighbor][y_neighbor]:
                grid_cost[x_neighbor][y_neighbor] = cost_new
                heapq.heappush(queue, (cost_new, x_neighbor, y_neighbor))
    return int(grid_cost[-1][-1])
