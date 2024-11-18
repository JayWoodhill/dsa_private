# reader.py
import os
import re
import numpy as np
from PIL import Image

def load_grids_from_images(folder_path, color_map):
    grids = []
    filenames = sorted(os.listdir(folder_path))
    
    for filename in filenames:
        if filename.endswith('.png'):
            # Extract grid dimensions from filename (e.g., grid_1_5x7.png)
            match = re.match(r'grid_\d+_(\d+)x(\d+)\.png', filename)
            if not match:
                continue
            rows, cols = int(match.group(1)), int(match.group(2))
            image_path = os.path.join(folder_path, filename)
            
            # Load the image using PIL and convert to NumPy array
            image = Image.open(image_path).convert('RGB')
            image_array = np.array(image)
            
            # Get image dimensions
            img_height, img_width, _ = image_array.shape
            
            # Calculate cell size
            cell_height = img_height // rows
            cell_width = img_width // cols

            # Initialize the grid
            grid = [[0 for _ in range(cols)] for _ in range(rows)]
            
            # Reverse color_map to map RGB to numbers
            rgb_to_num = {tuple(v): k for k, v in color_map.items()}
            
            # Process each cell
            for i in range(rows):
                for j in range(cols):
                    # Calculate the pixel range for the current cell
                    x0 = j * cell_width
                    y0 = i * cell_height
                    x1 = x0 + cell_width
                    y1 = y0 + cell_height
                    
                    # Extract the cell region
                    cell_region = image_array[y0:y1, x0:x1, :]
                    
                    # Calculate the average color of the cell
                    avg_color = cell_region.mean(axis=(0, 1)).astype(int)
                    avg_color = tuple(avg_color)
                    
                    # Map the average color to the numerical value
                    num = rgb_to_num.get(avg_color, -1)
                    if num == -1:
                        # Handle slight variations in color due to image saving
                        # Find the closest color in rgb_to_num
                        num = find_closest_color(avg_color, rgb_to_num)
                    
                    grid[i][j] = num
            grids.append(grid)
    return grids

def find_closest_color(color, rgb_to_num):
    min_distance = float('inf')
    closest_num = -1
    for rgb, num in rgb_to_num.items():
        distance = sum((c1 - c2) ** 2 for c1, c2 in zip(color, rgb))
        if distance < min_distance:
            min_distance = distance
            closest_num = num
    return closest_num
