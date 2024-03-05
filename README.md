# 15-puzzle-and-mechatronics
A mechatronics projects that physically solves 15-puzzle using a 3D printer and A* algorithm

Originally I planned to design the required 3-axis platform that executes the movements myself, but ended up modifying [this 3D printer DIY kit](https://m.tb.cn/h.5GNJoLrjbQtJI3J?sm=a5559a?tk=FMDXWPIbeJc ) instead (the kit was shipped from China). I also planned to use a RaspberryPi Zero 2 W is used to replace the MKS TinyBee to control the stepper motors, but ended up just generating gcode to put into the 3D printer as it was much easier.  

To use this repo, first modify the initial state here: [Code/A_star_solver/initial_state.txt](Code/A_star_solver/initial_state.txt). Please follow the same format. '0' denotes the the empty space. Optionally, the final state can also be modified here: [Code/A_star_solver/final_state.txt](Code/A_star_solver/final_state.txt). 

Next run [Code/A_star_solver/create_gcode.py](Code/A_star_solver/create_gcode.py). The program will print 'solvable' if the final state can be reached from the initial state. A file named 'output.gcode' will be generated. 

Before actually running this gcode, you will need to modify your 3D printer slightly. Mine happen to have a through-hole for me to shove in a pencil and secure it vertically with tape. Whether you do something sketchy like I did or want to design something is up to you, the key is to have something other than the nozzle contacting the puzzle pieces. Ideally the contact is something compliant (like rubber), so it can apply load properly. 

To run the code, first position your contactor (pencil in my case) centrally above the empty space represented by 0, then check that height is okay (contactor should be slightly less than 10mm above the puzzle pieces, you can slide over a piece to check). Now run the gcode and the 3D printer will solve the puzzle for you :) 

03/05/24: I plan to add a camera (once it gets shipped) to the setup so the initial state can be captured directly. I am too lazy to type it in myself xd

<br/><br/>
P.S. 

I did not write the A* algorithm, it is taken from [here](https://github.com/sanariaz154/15-puzzle-solver) with modification done to import initial and final state and export the path to final state. ChatGPT wrote [the piece](Code/A_star_solver/define_movement.py) that extracts the actual movement (up/down/left/right). I only really wrote the gcode generating bit. It seems in some cases, the puzzle is solvable but stack will overflow before finding the solution. I might look in this when I have time. 

Regarding mechatronics, the stepper motor driver has 1A current rating, which is below the motor's rating, so do remember to set the current limit. The 3D printer structural parts have questionable strength, I caused some to crack when tightening the bolts, and broken a piece when installing the fans. Super glue is strongly recommended as they can be very sketchy. 

For more info: 

Design of 3D printer and stl files of some structural parts available [here](https://www.thingiverse.com/thing:3447152). 

Extruder motor/fan info available [here](https://www.thingiverse.com/thing:2769783).

Skull fan cover available [here](https://www.thingiverse.com/thing:2502757) (Not a functional part, came with the kit, looks cool I guess) 

Assembly of the 3D printer followed [this video](https://www.bilibili.com/video/BV1u14y1h7F4/) (it's in Chinese) 

