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


class Animal:
    """General representation of animals."""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = weight
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + ' is delicious, yum!'
