import gzip
import shutil
import requests
import pandas as pd
import os
from utils.spiders_logevents import retrieve_logevent_month


def retrieve_abusefilter_logs_month(request_session, year, month, folder_path, filename=None):
    """
    Retrieve abusefiter & abusefilterblockeddomainhit logs for a specific month.
    Retrieved logs will be stored into a local csv file.
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
            
    Raises:
        - FileExistsError: If a file with the same name already exists.

    Returns:
        None. It writes the fetched data into to the disk.
    """

    # Retrieve and write
    retrieve_logevent_month(
        request_session=request_session,
        year=year,
        month=month,
        log_event_type='abusefilter',
        folder_path=folder_path,
        file_name=filename,
        prevent_overwrite=True
        )
    retrieve_logevent_month(
        request_session=request_session,
        year=year,
        month=month,
        log_event_type='abusefilterblockeddomainhit',
        folder_path=folder_path,
        file_name=filename,
        prevent_overwrite=False
        )


def retrieve_abusefilter_logs_year(request_session, year, folder_path):
    """
    Retrieve and store abusefilter logs for a specific year.

    Parameters:
        - year (int): The year for which logs should be retrieved.
        - folder_path (str): The folder path where the CSV files will be saved.

    Raises:
        - FileExistsError: If a file with the same name already exists.

    Returns:
        None
    """
    for month in range(1, 13):
        retrieve_abusefilter_logs_month(
            request_session=request_session,
            year=year,
            month=month,
            folder_path=folder_path)
