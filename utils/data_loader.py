from pathlib import Path
import pandas as pd


def file_iterator(dir_path, start_year, end_year, extract_cols):
    """
    Iterate through directories to find and read CSV files for specified years and months.

    This generator function looks for CSV files named according to a specific
    pattern (YYYY-MM.csv or YYYY-MM.csv.gz) within subdirectories for each year,
    reads them into Pandas DataFrames, and yields these DataFrames one at a time.
    If a file does not exist, it prints a message and yields None.

    Parameters:
    - dir_path (str): The base directory path where year directories are located.
    - start_year (int): The starting year of the range to process.
    - end_year (int): The ending year of the range to process.
    - usecols (list of str): Columns to read into the DataFrame from the CSV files.

    Yields:
    - pandas.DataFrame or None: A DataFrame constructed from the found CSV file
      for each month of each year in the range, or None if the file does not exist.

    Prints:
    - Messages indicating the status of file processing, including whether files
      are being extracted or if they're not found.
    """
    # Base directory path using pathlib for more idiomatic path handling
    dir_path = Path(dir_path)

    # Iterate through years and months
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            # Construct file path for both plain CSV and gzipped CSV
            f_path = dir_path / str(year) / f'{year}-{month:02d}.csv'
            f_path_gz = dir_path / str(year) / f'{year}-{month:02d}.csv.gz'
            
            # Check and yield CSV file
            if f_path.exists():
                print(f'Extracting: {f_path}')
                yield pd.read_csv(
                    f_path, usecols=extract_cols, on_bad_lines='warn'
                    )
            elif f_path_gz.exists():
                print(f'Extracting: {f_path_gz}')
                yield pd.read_csv(
                    f_path_gz, usecols=extract_cols, compression='gzip', on_bad_lines='warn'
                    )
            # Print error message if file not found
            else:
                print(f'File not found: {f_path}')
                print(f'File not found: {f_path_gz}')
                yield None
