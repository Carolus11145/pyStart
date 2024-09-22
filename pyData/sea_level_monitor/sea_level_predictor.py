import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import required data from the csv file
    df = pd.read_csv('epa-ea-level.csv')

    # Use matplotlib methods to design a scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    plt.plot()
    # Generate the first line of best fit
    best_fit = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    trend = [best_fit.slope * i + best_fit.intercept for i in df['Year']]
    df['trend'] = trend
    extended_yrs = [i for i in range(2014, 2051)]
    trend2 = [best_fit.slope * i + best_fit.intercept for i in extended_yrs]
    df2 = pd.DataFrame({'Year': extended_yrs, 'trend': trend2})

    df_merge = pd.concat([df, df2], ignore_index=True)
    plt.figure(figsize=(12, 6))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    plt.plot(df_merge['Year'],
             df_merge['CSIRO Adjusted Sea Level'], color='red')
    # Generate a new line of best fit
    df3 = df[(df['Year'] >= 2000)]

    best_fit2 = linregress(x=df3['Year'], y=df3['CSIRO Adjusted Sea Level'])
    df4 = df_merge[df_merge['Year'] >= 2000].copy(deep=True)
    trend3 = [best_fit2.slope * i + best_fit2.intercept for i in df4['Year']]
    df4['trend4'] = trend3
    plt.plot(df4['Year'], df4['trend4'], color='black')
    # Add the labels as well as title to the scatter plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
