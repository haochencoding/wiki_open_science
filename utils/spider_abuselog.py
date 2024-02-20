import gzip
import shutil
import requests
import pandas as pd
import os
from utils.file_processing import prevent_file_overwirte
from utils.file_processing import compress_csv
from utils.file_processing import generate_log_retrieval_dates


def retrieve_abuselog(
        request_session, start_date, end_date, continue_index=None
        ):
    """
    Send the request to retrieve logevents from Wikipedia API.

    Parameters:
        - url (str):
            - The URL of the Wikipedia API.
        - request_session (requests.Session):
            - A requests session object for making API requests.
        - start_date (str): 
            - The start date for the log retrieval (format: "YYYY-MM-DD").
        - end_date (str):
            - The end date for the log retrieval (format: "YYYY-MM-DD").
        - continue_index (dict):
            - A dictionary to continue retrieving abuse logs

    Returns:
        - logs (list): A list of logs retrieved from the API.
        - continue_index (dict): A dictionary to continue retrieving abuse logs.
    """
    # Set parameters for the API request, see link below for info on parameters
    # https://en.wikipedia.org/w/api.php?action=help&modules=query%2Blogevents
    url = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "format": "json",
        "list": "abuselog",
        "afllimit": "500",
        "aflstart": start_date,
        "aflend": end_date,
        "afldir": "newer"
    }

    # If it is a continued search request
    # Add search index into the request parameter
    if continue_index is not None:
        parameters['aflstart'] = continue_index['aflstart']

    # Send request
    r = request_session.get(url=url, params=parameters)

    # parse data to json
    data = r.json()
    # extract data
    logs = data['query']['abuselog']

    # Check if another request needs to be sent to fetch more data
    # If so, extract the continue variable for continued retrieval
    if 'continue' in data:
        continue_index = data['continue']
    # If not, set continue_variale to None
    else:
        continue_index = None

    return logs, continue_index


def retrieve_abuselog_month(
        request_session, year, month,
        folder_path, file_name=None, prevent_overwrite=True,
        compress=False
        ):
    """
    Retrieve and store logs into a local csv file for a specific month.
    Default format of the csv file name (year-month.csv)

    Parameters:
        - request_session (requests.Session):
            - A requests session object for making API requests.
        - year (int): 
            - The year for which logs are retrieved.
        - month (int):
            - The month for which logs are retrieved.
        - folder_path (str):
            - The folder path where the CSV file will be saved.
        - filename (str):
            - The CSV file name. Default to 'year-month.csv'
        - prevent_overwrite (bool):
            - If True, stop algorithm to prevent overwriting an existing file.
        - compress (bool): 
            - Specify if compress the CSV file into a gz file.

    Raises:
        - FileExistsError: If a file with the same name already exists.

    Returns:
        None. It writes the fetched data into to the disk.
    """
    total_logs = 0
    continue_index = None

    # Set the path of a local csv to store data
    if file_name is None:
        file_path = folder_path + f'{year}-{month:02d}.csv'
    else:
        file_path = folder_path + file_name

    # check if the file already exists to prevent overwrite
    if prevent_overwrite:
        prevent_file_overwirte(file_path)

    # Set dates for log retrieval
    start_date, end_date = generate_log_retrieval_dates(year, month)

    while True:
        # print out continue index
        if continue_index is not None:
            print(f'Search with continue index: {continue_index}', end=', ')

        # Send a request to retrieve block logs
        logs, continue_index = retrieve_abuselog(
            start_date=start_date,
            end_date=end_date,
            request_session=request_session,
            continue_index=continue_index
        )

        # Convert logs into a dataframe
        if len(logs) != 0:
            df = pd.DataFrame.from_records(logs)
            
            # Drop anon columns, as it can cause bad lines
            if 'anon' in df.columns:
                df = df.drop(['anon'], axis=1)

            # Ensure the directory exists. If not, create the directory
            if not os.path.exists(folder_path):
                print(f'{folder_path} directory does not exist')
                os.makedirs(folder_path, exist_ok=True)
                print(f'{folder_path} directory created to store data.')

            # Export the data to a local csv
            df.to_csv(file_path, mode='a', index=False)
            print(f'{len(df)} records retrieved.')
            
            # Update log count
            total_logs += len(df)
        else:
            print(f'0 records retrieved.')

        # Break the loop, when no continue index is returned
        if continue_index is None:
            print(f'Retrieval complete for logs between {start_date} and {end_date}.')
            if total_logs != 0:
                print(f'Total {total_logs} records retrieved & saved.')
            else:
                print(f'No record was retrieved or saved.')
            break

    if compress:
        compress_csv(file_path)


def retrieve_abuselog_year(year, folder_path, compress=False):
    """
    Retrieve and store abusefilter logs for a specific year.

    Parameters:
        - year (int): The year for which logs should be retrieved.
        - folder_path (str): The folder path where the CSV files will be saved.
        - compress (bool): 
            - Specify if compress the CSV file into a gz file.

    Raises:
        - FileExistsError: If a file with the same name already exists.

    Returns:
        None
    """
    for month in range(1, 13):
        s = requests.Session()
        retrieve_abuselog_month(
            request_session=s,
            year=year,
            month=month,
            folder_path=folder_path,
            compress=compress)
