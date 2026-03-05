** start of main.py **

def adjacency_list_to_matrix(adj_list):
    # Determine the number of nodes
    n = len(adj_list)
    
    # Initialize an n x n matrix filled with 0s
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill the matrix: for each node and its neighbors, set the entry to 1
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
            
    # Print each row in the matrix
    for row in matrix:
        print(row)
        
    return matrix




** end of main.py **

