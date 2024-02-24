from machine import Pin, Timer
import utime
import sys

steps_per_revolution = 200
 
# Initialize timer
tim = Timer()
 
def step(t):
    global step_pin
    step_pin.value(not step_pin.value())
 
def rotate_motor(delay):
    # Set up timer for stepping
    tim.init(freq=1000000//delay, mode=Timer.PERIODIC, callback=step)
 
def move(argument_from_pc):
    if argument_from_pc >= 0:
        # Set motor direction clockwise
        dir_pin.value(1)
    else:
        dir_pin.value(0)

    while True: 
        # Spin motor quickly
        rotate_motor(1000) #smaller num = faster
        utime.sleep_ms(steps_per_revolution)
        tim.deinit()  # stop the timer
        utime.sleep(1)

if len(sys.argv) > 1:

    # Retrieve the argument

    [axis,distance] = sys.argv[:]

    if axis == 'x':
        dir_pin = Pin(6, Pin.OUT)
        step_pin = Pin(5, Pin.OUT)
    elif axis == 'y':
        dir_pin = Pin(22,Pin.OUT)
        step_pin = Pin(27, Pin.OUT)
    elif axis == 'y':
        dir_pin = Pin(24,Pin.OUT)
        step_pin = Pin(23, Pin.OUT)

    move(distance)

else:

    print("No argument provided.")