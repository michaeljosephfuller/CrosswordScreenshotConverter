def specify_crossword_type(
    choices = ['Metro', 'Evening Standard']
) -> str:
    
    print('Crossword types:')
    for idx, choice in enumerate(choices):
        print(f'{idx}: {choice}')

    while True:
        try:
            idx_response = input(f'Choose the number of your crossword type:\n')
            idx = int(idx_response)
            if idx >= 0 and idx < len(choices):
                return choices[idx]
            else:
                raise Exception('Number not in the list, try again.')
        except ValueError:
            print('Must input an integer, try again.')
