# Excel Sheets Converter

Python tool for converting Excel files (`.xls` and `.xlsx`) into comma-separated CSV files.

## Repository contents

- `excel_sheets_convertor.py`: main conversion script.
- `convert_file.ipynb`: notebook containing the same process, intended for interactive execution.
- `mock_data/`: sample data for testing the conversion. It currently contains `mock_employees.xlsx` and `mock_places.xlsx`.

## Requirements

The project requires Python 3.9 or later, plus the dependencies listed in `requirements.txt`:

- `pandas`
- `openpyxl` for `.xlsx` files
- `xlrd` for `.xls` files

```bash
pip install -r requirements.txt
```

## Usage

Run the script inside the folder that contains the Excel files:

```bash
python excel_sheets_convertor.py
```
You also can run the script from the notebook file `excel_sheets_convertor.ipynb`


The script only searches for Excel files in its execution directory. To use the sample files in `mock_data/`, choose one of the following options:

1. Move `excel_sheets_convertor.py` into the `mock_data/` folder and run it there.
2. Move or copy the Excel files from `mock_data/` into the folder that contains `excel_sheets_convertor.py`.

The generated CSV files are saved in that same folder.

## How it works

Place the script in the same folder as the Excel files you want to convert. This script supports multiple files with the `.xls` and `.xlsx` extensions.

#### Output

- An Excel file with one sheet is converted to `OriginalFileName.csv`.
- An Excel file with multiple sheets creates one CSV file per sheet: `OriginalFileName_SheetName.csv`.

#### Processing messages

During execution, the script displays the following status messages:

1. `Processing file: {xls_file}`
2. `File converted: {csv_file}`
3. `Process completed successfully.`

#### Possible errors

| Situation | Message |
| --- | --- |
| No Excel files found | `No files with .xls or .xlsx extension found in the folder.` |
| Unsupported file format | `File format not supported. Must be .xls or .xlsx.` |
| Workbook has no sheets with data | `Excel file does not contain sheets with data.` |
| Unexpected read error | `Error reading Excel file: {error}` |
