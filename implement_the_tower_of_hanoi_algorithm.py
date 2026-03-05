** start of main.py **

def hanoi_solver(n):
    rod_1 = list(range(n, 0, -1))
    rod_2 = []
    rod_3 = []
    state = []

    def move(num_disks, source, destination, auxiliary):
        if num_disks > 0:
            # Move n-1 disks from source to auxiliary rod
            move(num_disks - 1, source, auxiliary, destination)
            # Move the largest remaining disk from source to destination rod
            disk = source.pop()
            destination.append(disk)
            # Record state after each disk movement
            state.append([list(rod_1), list(rod_2), list(rod_3)])
            # Move n-1 disks from auxiliary to destination rod
            move(num_disks - 1, auxiliary, destination, source)

    # Record the initial state
    state.append([list(rod_1), list(rod_2), list(rod_3)])
    # Start the recursive solving process
    move(n, rod_1, rod_3, rod_2)
    
    # Format output as string, with lists represented exactly as they are in Python
    # e.g., '[3, 2, 1] [] []'
    data = [f"{s[0]} {s[1]} {s[2]}" for s in state]
    return '\n'.join(data)

# Example usage (as provided in the user context)
# print(repr(hanoi_solver(2)))


** end of main.py **

