import heapq
import matplotlib.pyplot as plt

def read_input_files():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        start = int(lines[1].strip())
        goal = int(lines[2].strip())
        edges = []
        for line in lines[3:]:
            u, v, w = map(float, line.split())
            edges.append((int(u), int(v), w))
    return n, start, goal, edges

def read_coords():
    coords = []
    with open('coords.txt', 'r') as f:
        for line in f:
            x, y = map(float, line.split())
            coords.append((x, y))
    return coords

def dijkstra(n, start, goal, edges):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, w in edges:
        graph[u].append((v, w))
    
    distances = {i: float('inf') for i in range(1, n+1)}
    distances[start] = 0
    priority_queue = [(0, start)]
    predecessors = {i: None for i in range(1, n+1)}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct the shortest path
    path = []
    step = goal
    while step is not None:
        path.append(step)
        step = predecessors[step]
    path.reverse()
    
    return path, distances[goal]

def plot_path(coords, path):
    x, y = zip(*[coords[i-1] for i in path])
    plt.plot(x, y, 'ro-')
    plt.title("Shortest Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def main():
    n, start, goal, edges = read_input_files()
    coords = read_coords()
    
    path, cost = dijkstra(n, start, goal, edges)
    
    # Write to output.txt
    with open('17461873_output.txt', 'w') as f:
        f.write(" ".join(map(str, path)) + "\n")
        f.write(str(cost) + "\n")
    
    # Plot the path
    plot_path(coords, path)

if __name__ == "__main__":
    main()
