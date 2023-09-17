def is_dark_mode() -> bool:
    while True:
        try:
            response = input('Is your crossword screenshot in dark mode? (y/n)\n')
            if response.lower()[0] == 'y':
                return True
            elif response.lower()[0] == 'n':
                return False
            else:
                raise ValueError
        except ValueError:
            print('Must input y/n, try again.')
