from os import getcwd, listdir

PREV_DELIMITER = ';'
NEW_DELIMITER = ','
QUOTE_CHAR = '"'


def get_CSV_files()->list[str]:
    '''
    search in the same folder of this script for all the csv files
    store the name of these files in the variable files and return this list
    '''
    current_directory = getcwd()
    all_files = listdir(current_directory)
    csv_files = [filename for filename in all_files if filename.endswith('.csv')]

    return csv_files

def convert_delimiter(filename: str) -> list:
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            newContent = []
            for line in lines:
                row = line.strip().split(PREV_DELIMITER)
                newRow = map(parse_cell, row)
                newContent.append(NEW_DELIMITER.join(newRow))
        return newContent

    except FileNotFoundError:
        print('FILE NOT FOUND. CHECK FILE NAME')


def parse_cell(cell: str) -> str:
    '''
    If cell have coma inside, csv will generate missfunctions.
    This function wrap that cell. P.ex "cell"
    Args:
        cell (str): initial content of a cell
    Returns:
        cell (str): same content wraped with "" to aboid missfuntionalities 
    '''
    try:
        if NEW_DELIMITER in cell or PREV_DELIMITER in cell or QUOTE_CHAR in cell:
            cell = (QUOTE_CHAR + cell.replace(QUOTE_CHAR,
                    QUOTE_CHAR+QUOTE_CHAR) + QUOTE_CHAR)
        return cell
    except:
        print('ERROR: Could not parse cell')


def refill_CSV(file: str, content: list) -> None:
    '''
    generates or regenerates the File Document with the content
    Args:
        content (list): the content to fill the document
    Use of Global variables:
        FILENAME (str): the name of the file to extract data and refill
    Returns:
        None
    '''

    try:
        with open(file, 'w') as file:
            file.write('\n'.join(content))
    except:
        print('ERROR: Could not write the file')


if __name__ == '__main__':
    CSV_files = get_CSV_files()
    for file in CSV_files:
        new_content = convert_delimiter(file)
        refill_CSV(file, new_content)
