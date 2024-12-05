#!/usr/bin/python3
"""
This function returns the perimeter of the island described in grid.
grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1.
Cells are connected horizontally/vertically (not diagonally).
"""


def island_perimeter(grid):
    perimeter = 0

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check if the cell is land (1)
            if grid[i][j] == 1:
                # Check the 4 sides for exposure to water or edge
                if i == 0 or grid[i-1][j] == 0:  # check top
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:  # check bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # check left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:  # check right
                    perimeter += 1

    return perimeter
