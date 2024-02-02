import gzip
import shutil
import requests
import pandas as pd
import os


def compress_csv(file_path):
    """
    Compress a file using gzip compression.

    Parameters:
        - file_path (str): The path of the file to be compressed.

    Returns:
        - None. It writes the compressed file to the disk.
    """
    with open(file_path, 'rb') as f_in, gzip.open(f'{file_path}.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


def retrieve_block_logs(request_session, start_date, end_date,
                        continue_index=None):
    """
    Send the request to retrieve blocking logs from Wikipedia API.

    Parameters:
        - url (str):
            - The URL of the Wikipedia API.
        - request_session (requests.Session):
            - A requests session object for making API requests.
        - start_date (str): 
            - The start date for the log retrieval (format: "YYYY-MM-DD").
        - end_date (str):
            - The end date for the log retrieval (format: "YYYY-MM-DD").

    Returns:
        - logs (list): A list of blocking logs retrieved from the API.
        - continue_index (str):
            - A token provided by the API to facilitate continued searching
            - Useful when a single request cannot retrieve all the requested data in one API query.
    """
    # Set parameters for the API request, see link below for info on parameters
    # https://en.wikipedia.org/w/api.php?action=help&modules=query%2Blogevents
    url = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "format": "json",
        "list": "logevents",
        "lelimit": "500",
        "letype": "block",
        "lestart": start_date,
        "leend": end_date,
        "ledir": "newer"
    }

    # If it is a continued search request
    # Add search index into the request parameter
    if continue_index is not None:
        parameters['lecontinue'] = continue_index

    # Send request
    r = request_session.get(url=url, params=parameters)

    # parse data to json
    data = r.json()
    # extract data on blocking logs
    logs = data["query"]["logevents"]

    # Check if another request needs to be sent to fetch more data
    # If so, extract the continue variable for continued retrieval
    if 'continue' in data:
        continue_index = data['continue']['lecontinue']
    # If not, set continue_variale to None
    else:
        continue_index = None

    return logs, continue_index


def retrieve_block_logs_month(year, month, folder_path, compress=False):
    """
    Retrieve and store block logs into a local csv file for a specific month.
    Format of the name of local file (year-month.csv)

    Parameters:
        - year (int): 
            - The year for which block logs should be retrieved.
        - month (int):
            - The month for which block logs should be retrieved.
        - folder_path (str):
            - The folder path where the CSV file will be saved.
        - compress (bool): 
            - Specify if compress the CSV file into a gz file.

    Raises:
        - FileExistsError: If a file with the same name already exists.

    Returns:
        None. It writes the fetched data into to the disk.
    """
    # Set dates for log retrieval
    if month < 12:
        next_month = month + 1
        start_date = f'{year}-{month:02d}-01T00:00:00Z'
        end_date = f'{year}-{next_month:02d}-01T00:00:00Z'
    else:
        start_date = f'{year}-{month:02d}-01T00:00:00Z'
        end_date = f'{year + 1}-01-01T00:00:00Z'

    # Initialise request session
    s = requests.Session()
    total_logs = 0
    continue_index = None

    # Set the path of a local csv to store data
    file_path = folder_path + f'{year}-{month:02d}.csv'

    # Check if a file already exists
    if os.path.exists(file_path):
        print(f"{file_path} already exists. Cannot overwrite.")
        raise FileExistsError(f'Pls check if a {file_path} already exists on local disk.')

    while True:
        # print out continue index
        if continue_index is not None:
            print(f'Search with continue index: {continue_index}', end=', ')

        # Send a request to retrieve block logs
        logs, continue_index = retrieve_block_logs(
            start_date=start_date,
            end_date=end_date,
            request_session=s,
            continue_index=continue_index
        )

        # Convert logs into a dataframe
        df = pd.DataFrame.from_records(logs)

        # Export the data to a local csv
        df.to_csv(file_path, mode='a', index=False)
        print(f'{len(df)} records retrieved.')

        # Update log count
        total_logs += len(df)

        # Break the loop, when no continue index is returned
        if continue_index is None:
            print(f'Retrieval complete for logs between {start_date} and {end_date}.')
            print(f'{total_logs} records retrieved.')
            break

    if compress:
        compress_csv(file_path)


def retrieve_block_logs_year(year, folder_path, compress=False):
    """
    Retrieve and store block logs for a specific year.

    Parameters:
        - year (int): The year for which block logs should be retrieved.
        - folder_path (str): The folder path where the CSV files will be saved.

    Raises:
        - FileExistsError: If a file with the same name already exists.

    Returns:
        None
    """
    for month in range(1, 13, 1):
        retrieve_block_logs_month(year, month, folder_path, compress=compress)
