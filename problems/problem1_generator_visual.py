import random
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image

def generate_random_grid(max_size=15, max_colors=4):
    """
    Generates a random grid with dimensions up to max_size x max_size.
    The grid cells are filled with random color values.

    Parameters:
    - max_size (int): Maximum size for the grid dimensions (rows and columns).
    - max_colors (int): Maximum number of different colors to use.

    Returns:
    - tuple: A tuple containing (number of rows, number of columns, grid as a list).
    """
    # Randomly choose dimensions between 1 and max_size
    rows = random.randint(1, max_size)
    cols = random.randint(1, max_size)

    # Generate the grid with random color values
    grid = [[random.randint(1, max_colors) for _ in range(cols)] for _ in range(rows)]

    return rows, cols, grid

def generate_grids_images(num_grids=100, max_size=15, max_colors=4):
    """
    Generates multiple grids and saves them as image files.
    Prompts the user for the output folder using a directory selection dialog.

    Parameters:
    - num_grids (int): The number of grids to generate.
    - max_size (int): Maximum size for the grid dimensions.
    - max_colors (int): Maximum number of different colors to use.
    """
    # Use tkinter to open a directory selection dialog
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user for the output folder
    folder_selected = filedialog.askdirectory(
        title="Select Output Folder for Grid Images"
    )

    if not folder_selected:
        print("No folder selected. Operation cancelled.")
        return

    # Define colors for the cells (adjust or add more as needed)
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

    # Ensure we have enough colors for the number of colors used
    if max_colors > len(color_map):
        print(f"Error: max_colors ({max_colors}) exceeds the number of defined colors ({len(color_map)}).")
        return

    # Generate grids and save as images
    for i in range(num_grids):
        rows, cols, grid = generate_random_grid(max_size, max_colors)

        # Create a new image with the appropriate size
        cell_size = 20  # Size of each cell in pixels
        img_width = cols * cell_size
        img_height = rows * cell_size
        image = Image.new('RGB', (img_width, img_height), color='white')

        # Draw the grid
        for row in range(rows):
            for col in range(cols):
                color_value = grid[row][col]
                color = color_map[color_value]
                # Define the bounding box of the cell
                x0 = col * cell_size
                y0 = row * cell_size
                x1 = x0 + cell_size
                y1 = y0 + cell_size
                # Fill the cell with the corresponding color
                for x in range(x0, x1):
                    for y in range(y0, y1):
                        image.putpixel((x, y), color)

        # Save the image
        image_filename = f"grid_{i+1}_{rows}x{cols}.png"
        image_path = os.path.join(folder_selected, image_filename)
        image.save(image_path)

    print(f"Generated {num_grids} grid images and saved to '{folder_selected}'.")

# Generate the grid images
generate_grids_images(num_grids=100, max_size=15, max_colors=4)
