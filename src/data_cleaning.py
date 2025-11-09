"""
data_cleaning.py
----------------
This module handles data preprocessing for the Netflix dataset:
- Removing duplicates
- Filling missing values
- Converting date formats
"""

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the Netflix dataset and return the cleaned DataFrame."""
    df = df.drop_duplicates()
    df['country'] = df['country'].fillna('Unknown')
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df
