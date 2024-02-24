# 15-puzzle-and-mechatronics
A mechatronics projects that physically solves 15-puzzle with A* 

Originally I planned to design the required 3-axis platform that executes the movements myself, but ended up modifying [this 3D printer DIY kit](https://m.tb.cn/h.5GNJoLrjbQtJI3J?sm=a5559a?tk=FMDXWPIbeJc )
instead (the kit was shipped from China). A RaspberryPi Zero 2 W is used to replace the MKS TinyBee to control the stepper motors because I only know Python. 

The intent is to use the PC to calculate the required movement steps (with A*), connect the RPi via SSH and transfer the commands, then use RPi to control the stepper motors and execute the movement. (Supposedly I could do it all in RPi, but for development purposes it's a bit convoluted, feel free to modify the sequence however you want). 

A* algorithm is taken from: [https://github.com/nrupeshsurya/16-puzzle-problem](https://github.com/nrupeshsurya/16-puzzle-problem) with modification done to import goal state as well. 
