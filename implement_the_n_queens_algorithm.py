** start of main.py **

def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    stack = [[]]
    
    while stack:
        current = stack.pop()
        row = len(current)
        
        if row == n:
            solutions.append(current)
        else:
            for col in range(n - 1, -1, -1):
                if is_safe(current, row, col):
                    stack.append(current + [col])
    
    return solutions

def is_safe(placement, row, col):
    for r, c in enumerate(placement):
        if c == col:
            return False
        if abs(row - r) == abs(col - c):
            return False
    return True

** end of main.py **

