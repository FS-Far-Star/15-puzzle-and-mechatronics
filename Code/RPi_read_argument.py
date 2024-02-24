# 1.py on the Raspberry Pi

import sys

if __name__ == "__main__":

    # Check if an argument is provided

    if len(sys.argv) > 1:

        # Retrieve the argument

        argument_from_pc = sys.argv[1]

        print(f"Received argument from PC: {argument_from_pc}")

        # Further processing or writing to a file can be done here

        with open('/home/wraith/Desktop/output.txt', 'w') as file:

            file.write(argument_from_pc)

    else:

        print("No argument provided.")