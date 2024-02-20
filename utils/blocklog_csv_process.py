import pandas as pd
import re


def check_ip_address(df, column):
    # Regular expression for matching IPv4 & IPv6 addresses with non-capturing groups
    ipv4_pattern = r'(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    ipv6_pattern = r'(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}(?:\/\d{1,3})?'
    ip_pattern = f'(?:{ipv4_pattern}|{ipv6_pattern})'

    return df[column].str.contains(ip_pattern, regex=True)


