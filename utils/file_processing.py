import shutil
import os
import gzip

def compress_csv(file_path):
    """
    Compress a file using gzip compression.

    Parameters:
        - file_path (str): The path of the file to be compressed.

    Returns:
        - None. It writes the compressed file to the disk.
    """
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f_in, gzip.open(f'{file_path}.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'{file_path} compressed into gzip file.')


def prevent_file_overwirte(file_path):
    # Check if a file already exists
    if os.path.exists(file_path):
        print(f"{file_path} already exists. Cannot overwrite.")
        raise FileExistsError(f'Pls check if a {file_path} already exists on local disk.')


def generate_log_retrieval_dates(year, month):
    """
    Generate start and end dates for log retrieval based on the given year and month.

    Parameters:
        year (int): The year for log retrieval.
        month (int): The month for log retrieval.

    Returns:
        tuple: A tuple containing the start and end dates as strings in the format 'YYYY-MM-DDT00:00:00Z'.
    """
    if month < 12:
        next_month = month + 1
        start_date = f'{year}-{month:02d}-01T00:00:00Z'
        end_date = f'{year}-{next_month:02d}-01T00:00:00Z'
    else:
        start_date = f'{year}-{month:02d}-01T00:00:00Z'
        end_date = f'{year + 1}-01-01T00:00:00Z'
    return start_date, end_date