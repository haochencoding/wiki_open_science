import pandas as pd
import re

def clean_df(df):
    df = df.drop_duplicates()
    # remove rows containing the column names
    df = df[df['title']!='title']
    # remove rows containing missing information on user/administrator names
    df = df[~df['title'].isna() & ~df['user'].isna()]
    # remove 'User:' string from the title column
    df['title'] = df['title'].str[5:]
    # remove rows where the administrator block and unblock themselves
    df = df[df['user'] != df['title']]
    return df

def check_ip_address(df, column):
    # Regular expression for matching IPv4 & IPv6 addresses with non-capturing groups
    ipv4_pattern = r'(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    ipv6_pattern = r'(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}(?:\/\d{1,3})?'
    ip_pattern = f'(?:{ipv4_pattern}|{ipv6_pattern})'

    return df[column].str.contains(ip_pattern, regex=True)


