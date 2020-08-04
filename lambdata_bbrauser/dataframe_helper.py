"""
Some function to help cleaning and handling dataframes.
"""

import pandas as pd
import numpy as np


def report_missing_values(df):
    """Print a pretty report of missing values."""
    df = df.isnull().sum()
    df = pd.DataFrame(df, columns=['Number Missing'])
    return df


def date_split(df):
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df['Day'] = pd.DatetimeIndex(df['Date']).day
    df['Year'] = pd.DatetimeIndex(df['Date']).year
    return df
