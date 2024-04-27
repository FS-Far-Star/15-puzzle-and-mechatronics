# Function to find the position of the empty tile (0) in the puzzle
def find_empty_tile(puzzle):
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0:
                return i, j

# Function to determine the movement needed to transition from one state to another
def determine_movement(current_state, next_state):
    current_empty_row, current_empty_col = find_empty_tile(current_state)
    next_empty_row, next_empty_col = find_empty_tile(next_state)

    # Movement directions: Up, Down, Left, Right
    movements = [(1, 0, 'Up'), (-1, 0, 'Down'), (0, 1, 'Left'), (0, -1, 'Right')]

    for dr, dc, movement in movements:
        if current_empty_row + dr == next_empty_row and current_empty_col + dc == next_empty_col:
            return movement

def extract_movements():
    # Read states from the text file
    with open('A_star_solver/path.txt', 'r') as file:
        states = [eval(line) for line in file]

    # Determine movements between consecutive states
    movements_list = []
    for i in range(len(states) - 1):
        current_state = states[i]
        next_state = states[i + 1]
        movement = determine_movement(current_state, next_state)
        movements_list.append(movement)

    # Save the list of movements to 'movements.txt'
    with open('A_star_solver/movements.txt', 'w') as file:
        for movement in movements_list:
            file.write(movement + '\n')

    # Return the list of movements
    # print("List of movements:", movements_list)

if __name__ == '__main__':
     extract_movements()