from A_star_solver import Astar
from A_star_solver import define_movement
from A_star_solver import create_gcode
from web_connect import *
from PC_get_picture_from_Pi import *
from Image_processing import*
from OCR import *
import os

if __name__ == '__main__':
    get_picture()
    image_preprocess()
    perform_ocr()
    Astar.A_star_go()
    define_movement.extract_movements()
    create_gcode.get_gcode_file()
    send_instructions()
    os.remove("current_state.jpg")
    os.remove("processed.jpg")
    os.remove("A_star_solver/initial_state.txt")
    os.remove("processed.jpg")
