** start of main.py **

def dfs(graph, node):
    visited = []
    stack = [node]
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            for neighbor, connected in enumerate(graph[current]):
                if connected and neighbor not in visited:
                    stack.append(neighbor)
    
    return visited




** end of main.py **

