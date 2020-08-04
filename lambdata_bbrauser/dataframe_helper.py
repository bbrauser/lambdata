"""
Some function to help cleaning and handling dataframes.
"""

import pandas as pd

def report_missing_values(df):
    """Print a pretty report of missing values."""
    df = df.isnull().sum()
    df = pd.DataFrame(df, columns = ['Number Missing'])
    return df

def tvt_split(df):
     X_train, y_train, X_val, y_val = train_test_split(train, train_size=0.8, test_size=0.2, random_state=42)