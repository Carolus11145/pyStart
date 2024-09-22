import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import required data from the csv file
    df = pd.read_csv('epa-sea-level.csv')

    # Use matplotlib methods to design a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    plt.plot()
    # Show the linear regression for all the given data
    m = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extended_yrs = pd.Series(range(1880, 2051))
    levels_pred = m.intercept + m.slope * extended_yrs
    plt.plot(extended_yrs, levels_pred, color='red', label='Linear Regression For All Data')

    # Create a display of the linear regression for the most recent data
    recent = df[df['Year'] >= 2000]
    m2 = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    recent_yrs = pd.Series(range(2000, 2051))
    recent_pred = m2.intercept + m2.slope * recent_yrs
    plt.plot(recent_yrs, recent_pred, color='green', label='Linear Regression For Recent Data')
    # Add the labels as well as title to the scatter plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
