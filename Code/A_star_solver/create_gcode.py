from Astar import *
from define_movement import *

def generate_gcode(movements):
    # Initialize an empty list to store the generated G-code commands
    gcode_lines = []

    # Add command to set relative movement mode
    gcode_lines.append('G91')

    # Check the direction of movement
    for i in range(0,len(movements)):
        if movements[i] == 'Up':
            gcode_lines.append('G1 Y-30')  # Move -30mm in Y axis 
            gcode_lines.append('G1 Z-10')  # Move -10mm in Z axis
            gcode_lines.append('G1 Y+30')  # Move +30mm in Y axis
            gcode_lines.append('G1 Z+10')  # Move +10mm in Z axis
            gcode_lines.append('G1 Y-30')  # Move -30mm in Y axis 
        elif movements[i] == 'Down':
            gcode_lines.append('G1 Y+30')  # Move +30mm in Y axis 
            gcode_lines.append('G1 Z-10')  # Move -10mm in Z axis
            gcode_lines.append('G1 Y-30')  # Move -30mm in Y axis
            gcode_lines.append('G1 Z+10')  # Move +10mm in Z axis
            gcode_lines.append('G1 Y+30')  # Move +30mm in Y axis 
        elif movements[i] == 'Left':
            gcode_lines.append('G1 X+30')  # Move +30mm in X axis 
            gcode_lines.append('G1 Z-10')  # Move -10mm in Z axis
            gcode_lines.append('G1 X-30')  # Move +30mm in X axis
            gcode_lines.append('G1 Z+10')  # Move +10mm in Z axis
            gcode_lines.append('G1 X+30')  # Move +30mm in X axis 
        elif movements[i] == 'Right':
            gcode_lines.append('G1 X-30')  # Move +30mm in X axis 
            gcode_lines.append('G1 Z-10')  # Move -10mm in Z axis
            gcode_lines.append('G1 X+30')  # Move -30mm in X axis
            gcode_lines.append('G1 Z+10')  # Move +10mm in Z axis
            gcode_lines.append('G1 X-30')  # Move +30mm in X axis 

    gcode_lines.append('G1 Z+100')
    # Return the list of generated G-code commands
    return gcode_lines

def get_gcode_file():
    A_star_go()
    extract_movements()
    # Initialize an empty list to store the movements
    movements_list = []
    # Open the file and read its contents
    with open('movements.txt', 'r') as file:
        # Read each line from the file
        for line in file:
            # Append each line (movement) to the list, removing leading/trailing whitespace
            movements_list.append(line.strip())

    # Generate G-code commands
    gcode_commands = generate_gcode(movements_list)

    # Write G-code commands to a file
    with open('output.gcode', 'w') as f:
        # Write each G-code line to the file
        for line in gcode_commands:
            f.write(line + '\n')

if __name__ == '__main__':
     get_gcode_file()