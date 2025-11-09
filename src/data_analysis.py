"""
data_analysis.py
----------------
Contains helper functions to summarize and explore Netflix dataset.
"""

import pandas as pd

def basic_summary(df: pd.DataFrame):
    """Print key dataset summaries."""
    print("### Dataset Info ###")
    print(df.info())
    print("\n### Missing Values per Column ###")
    print(df.isnull().sum())
    print("\n### Descriptive Statistics ###")
    print(df.describe(include='all').T)

def quick_insights(df: pd.DataFrame):
    """Return simple insights like counts and top categories."""
    summary = {
        "Movies_vs_TVShows": df['type'].value_counts(),
        "Top_Countries": df['country'].value_counts().head(10),
        "Top_Ratings": df['rating'].value_counts().head(10)
    }
    return summary
