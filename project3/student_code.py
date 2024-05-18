import heapq
import math

def shortest_path(M, start, goal):
    """Generate the shortest path from start to goal intersection"""
    intersections = M.intersections
    roads = M.roads
    
    # Dictionaries to store the cost to reach each node and the taken path
    came_from = {}
    current_cost = {}
    came_from[start] = None
    current_cost[start] = 0

    # Priority queue to keep track of nodes to explore
    frontier = []
    heapq.heappush(frontier, (0, start))
    
    while frontier:
        _, current_node = heapq.heappop(frontier)
        
        if current_node == goal:
            # Arrived at the goal intersection
            break
        
        for neighbor in roads[current_node]:
            # Find the nearest neighbor
            new_cost = current_cost[current_node] + euclidean_distance(intersections[current_node], intersections[neighbor])
            
            if neighbor not in current_cost or new_cost < current_cost[neighbor]:
                current_cost[neighbor] = new_cost
                priority = new_cost + euclidean_distance(intersections[neighbor], intersections[goal])
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node
    
    # Reconstruct path
    current = goal
    result = []

    while current is not None:
        result.append(current)
        current = came_from[current]

    result.reverse()

    return result

def euclidean_distance(start, end):
    """Calculate the distance between two intersections"""
    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
