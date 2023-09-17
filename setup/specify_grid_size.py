def specify_grid_size() -> int:
    while True:
        try:
            grid_size = input('Specify the grid size of your crossword:\n')
            return int(grid_size)
        except ValueError:
            print('Must input an integer, try again.')
