import time

from setup.is_dark_mode import is_dark_mode
from setup.specify_crossword_type import specify_crossword_type
from setup.specify_grid_size import specify_grid_size

from converter.converter import Converter


def main():
    
    print('Welcome to the Crossword Screenshot Converter.')
    print('Before continuing, please add your crossword screenshot to the PUT_SCREENSHOT_HERE folder.')
    print('Use the filename YYYY-MM-DD.png, e.g. 2023-08-28.png.\n')
    
    crossword_date = time.strftime('%Y-%m-%d')
    grid_size: int = specify_grid_size()
    dark_mode: bool = is_dark_mode()
    #crossword_type: str = specify_crossword_type(),

    converter = Converter(
        crossword_date=crossword_date,
        grid_size=grid_size,
        dark_mode=dark_mode,
        #crossword_type=crossword_type,
    )

    converter.convert_crossword_screenshot_to_df()
    # print(converter.crossword_df)

    converter.create_crossword_xlsx()

if __name__ == "__main__":
    main()