"""
Update below functions with code to print different grids based on the input parameters.

NOTE: do not print anything besides the grid boxes in your functions.
"""


# PART 1 - prints a simple 2x2 grid with an interior cell size of 4
def print_grid1():
    level = "+----+----+"  # creates a horizontal levels
    wall = "|    |    |"  # creates a section of the vertical walls
    for i in range(2):  # sets the grid size at 2x2
        print(level)
        for i in range(4):  # sets the wall height at 4
            print(wall)
    print(level)


# PART 2 - prints a 2x2 grid with a variable interior cell size
def print_grid2(size):
    origin = "+"  # sets the initial symbol in the horizontal level
    level_panel = (
        size * "-"
    ) + origin  # sets the remainder of the horizontal level using the size variable to control for the interior cell size
    wall = "|"  # sets the initial symbol for each section of vertical wall
    wall_panel = (
        size * " "
    ) + wall  # sets the remainder of each section of vertical wall using the size variable to control for the interior cell size
    for i in range(2):  # sets the grid height to 2 cells
        print(origin + (level_panel * 2))  # sets the grid width to 2 cells
        for i in range(size):  # sets the wall height to the correct interior cell size
            print(wall + (wall_panel * 2))  # maintains the grid width to 2 dells
    print(
        origin + (level_panel * 2)
    )  # adds the floor of the grid, maintaining the grid width


# PART 3 - prints a grid of variable size with a variable interior cell size
def print_grid3(box_size, cell_size):
    origin = "+"  # sets the initial symbol in the horizontal level
    level_panel = (
        cell_size * "-"
    ) + origin  # sets the remainder of the horizontal level using the size variable to control for the interior cell size
    wall = "|"  # sets the initial symbol for each section of vertical wall
    wall_panel = (
        cell_size * " "
    ) + wall  # sets the remainder of each section of vertical wall using the size variable to control for the interior cell size
    for i in range(
        box_size
    ):  # sets the grid height to the value of the box_size variable
        print(
            origin + (level_panel * box_size)
        )  # sets the grid width to the value of the box_size veriable
        for i in range(
            cell_size
        ):  # sets the wall height to the correct interior cell size
            print(
                wall + (wall_panel * box_size)
            )  # maintains the grid witdh to the value of the box_size variable
    print(
        origin + (level_panel * box_size)
    )  # adds the floor of the grid, maintaining the grid width


# PART 4 - prints a rectangular grid of variable size with rectangular cells with variable interior sizes
def print_grid4(grid_width, grid_height, cell_width, cell_height):
    origin = "+"  # sets the initial symbol in the horizontal level
    level_panel = (
        cell_width * "-"
    ) + origin  # sets the remainder of the horizontal level using the cell_width variable
    wall = "|"  # sets the initial symbol for each section of vertical wall
    wall_panel = (
        cell_width * " "
    ) + wall  # sets the remainder of each section of vertical wall using the cell_width variable
    for i in range(grid_height):  # sets the grid height
        print(origin + (level_panel * grid_width))  # sets the grid width
        for i in range(cell_height):  # sets the cell wall height
            print(wall + (wall_panel * grid_width))  # maintains the grid width
    print(
        origin + (level_panel * grid_width)
    )  # adds the floor of the grid, maintaining the grid width


# executes your grid functions below
if __name__ == "__main__":
    print_grid1()

    print_grid2(3)

    print_grid3(5, 1)

    print_grid4(4, 2, 15, 3)
