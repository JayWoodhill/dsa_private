# main.py
import os
from reader import load_grids_from_images
#from config.config_functions import profile_function, system_info
from problem1_solver import largest_contiguous_block

# Define the color map used in image generation
color_map = {
    1: (255, 255, 0),   # Yellow
    2: (0, 128, 0),     # Green
    3: (255, 165, 0),   # Orange
    4: (128, 0, 128),   # Purple
    5: (255, 192, 203), # Pink
    6: (0, 255, 255),   # Cyan
    7: (255, 0, 0),     # Red
    8: (0, 0, 255),     # Blue
    9: (128, 128, 128), # Gray
    10: (0, 0, 0),      # Black
}

'''# image source
folder_path = 'dsa_private/problems/problem1_grids'

system_info()

grids = load_grids_from_images(folder_path, color_map)

for idx, grid in enumerate(grids):
    @profile_function
    def process_grid(grid, idx):
        max_block_size = largest_contiguous_block(grid)
        print(f"Grid #{idx + 1}: Largest contiguous block area is {max_block_size}")
    process_grid(grid, idx)
'''

# Image source
folder_path = 'dsa_private/problems/problem1_grids'

grids = load_grids_from_images(folder_path, color_map)

for idx, grid in enumerate(grids):
    max_block_size = largest_contiguous_block(grid)
    print(f"Grid #{idx + 1}: Largest contiguous block area is {max_block_size}")