import numpy as np

def generate_gcode(movements):
    # Initialize an empty list to store the generated G-code commands
    gcode_lines = []

    # set initial location
    gcode_lines.append('G28 X Y')
    gcode_lines.append('G92 X0 Y0 Z200')
    gcode_lines.append('G90')

    l = 0
    with open('A_star_solver/initial_state.txt', 'r') as my_file:
    # Read each line from the file
        for line in my_file:
            # Split each line into elements
            elements = line.strip().split()
            # Convert elements to integers
            row = [int(x) for x in elements]
            try:
                a,b = l,row.index(0)
            except ValueError:
                pass
            l = l+1
         
    x_loc = 64 + b *30
    y_loc = 102 + a *30
    gcode_lines.append('G1 X'+str(x_loc)+' Y'+str(y_loc)+' Z85')

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

    gcode_lines.append('G90')
    gcode_lines.append('G0 X0 Y0 Z200')
    # Return the list of generated G-code commands
    return gcode_lines

def get_gcode_file():
    # Initialize an empty list to store the movements
    movements_list = []
    # Open the file and read its contents
    with open('A_star_solver/movements.txt', 'r') as file:
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