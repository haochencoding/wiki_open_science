import pandas as pd
from utils.data_loader import file_iterator


def extract_administrator_names(dir_path, start_year, end_year):
    """
    Extracts and returns names of administrators that block users from CSV files.

    This function iterates over a series of CSV files located within a directory
    path. These files are expected to span a range of years, from start_year to
    end_year, inclusive. Each file is processed to extract 'user' names, 
    corresponding to administrators blocking users.

    Parameters:
    - dir_path (str): The directory path where the CSV files are located.
    - start_year (int): The starting year of the files to be processed.
    - end_year (int): The ending year of the files to be processed.

    Returns:
    - a list of administrator names
    """
    # Define the columns to extract from the CSV files
    extracted_columns = ['user']

    # Initialize sets to store unique names of administrators
    administrators = set()

    # Iterate over files returned by the file_iterator generator
    for _, df in file_iterator(dir_path, start_year, end_year, extract_cols=extracted_columns):
        if df is not None:
            administrators.update(set(df['user']))

    return list(administrators)


def extract_blocked_editor_names(dir_path, start_year, end_year):
    """
    Extracts and returns names of bloced editors from CSV files.

    This function iterates over a series of CSV files located within a directory
    path. These files are expected to span a range of years, from start_year to
    end_year, inclusive. Each file is processed to extract 'title' column, 
    corresponding to the name of blocked user.

    Parameters:
    - dir_path (str): The directory path where the CSV files are located.
    - start_year (int): The starting year of the files to be processed.
    - end_year (int): The ending year of the files to be processed.

    Returns:
    - a list of editor names
    """
    # Define the columns to extract from the CSV files
    extracted_columns = ['title']

    # Initialize sets to store unique names of administrators
    blocked_editors = set()

    # Iterate over files returned by the file_iterator generator
    for _, df in file_iterator(dir_path, start_year, end_year, extract_cols=extracted_columns):
        if df is not None:
            blocked_editors.update(set(df['title']))

    return list(blocked_editors)
