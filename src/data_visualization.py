"""
data_visualization.py
---------------------
This module creates visualizations for Netflix dataset analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_content_type(df):
    sns.countplot(data=df, x='type', palette='viridis')
    plt.title('Distribution of Movies and TV Shows on Netflix')
    plt.xlabel('Content Type')
    plt.ylabel('Count')
    plt.show()

def plot_top_countries(df):
    top_countries = df['country'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='mako')
    plt.title('Top 10 Countries with Most Netflix Titles')
    plt.xlabel('Number of Titles')
    plt.ylabel('Country')
    plt.show()

def plot_year_added(df):
    plt.figure(figsize=(12,6))
    sns.histplot(df['year_added'].dropna(), bins=20, kde=True, color='coral')
    plt.title('Content Added to Netflix Over the Years')
    plt.xlabel('Year Added')
    plt.ylabel('Number of Titles Added')
    plt.show()
