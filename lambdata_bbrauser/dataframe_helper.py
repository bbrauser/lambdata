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


# class Animal:
#     """General representation of animals."""
#     def __init__(self, name, weight, color):
#         self.name = str(name)
#         self.weight = weight
#         self.color = color

#     def run(self):
#         return 'Vroom!'

#     def eat(self, food):
#         return food + ' is delicious, yum!'


class MathFunctions:
    """Basic math function to add, subtract, multiply and divide"""
    def __init__(self, num1):
        self.n1 = num1

    def addition(self, num2):
        self.n1 += num2
        return self.n1

    def subtract(self, num2):
        self.n1 -= num2
        return self.n1

    def multiply(self, num2):
        self.n1 *= num2
        return self.n1

    def divide(self, num2):
        self.n1 /= num2
        return self.n1

    def __repr__(self):
        return '{}'.format(self.n1)
