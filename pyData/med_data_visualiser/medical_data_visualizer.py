import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import the required data from the medical examinations csv file
df = pd.read_csv('medical_examination.csv')

# Add an overweight column to the dataframe of the medical examinations
df['overweight'] = (df['weight'] / (df['height'] / 100) **
                    2).apply(lambda x: 0 if x < 25 else 1)

# Normalise the data in such a way that 0 is always a 'good' outcome and 1 is always a 'bad' outcome
df['cholesterol'] = df['cholesterol'].apply(
    lambda x: 0 if x == 1 else 1)  # Normalises the cholesterol data set
# Normalises the glucose data set
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Design a categorical plot using the function below:


def draw_cat_plot():
    # Create a dataframe for the cat plot via us of the pd.melt method.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Reformat and group the data in df_cat by splitting it at cardio. For each feature show the counts, and rename one of the columns so the catplot works correctly
    df_cat['total'] = 1
    df_cat = df_cat.groupby(
        ['variable', 'cardio', 'value'], as_index=False).count()

    # Utilise the sns.catplot method to convert the data into long format and create a chart which shows the value counts of the categorical features
    draw_cat = sns.catplot(
        x='variable', y='total', hue='value', data=df_cat, col='cardio', kind='bar')
    # Obtain the figure output and store it in the fig variable
    fig = draw_cat.fig

    # These two lines must not be altered, as they are important in the function's performance
    fig.savefig('catplot.png')
    return fig


# Design the heat map by using the function below
def draw_heat_map():
    # Filter out the patient segments in the heat dataframe which contain the incorrect information
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(
        0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix of the heat dataframe
    corr = df_heat.corr()

    # Use the mask variable to generate and store a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Using sns.heatmap, plot the correlation matrix of the dataframe
    ax = sns.heatmap(corr, mask=mask, vmax=.25, fmt='.1f', center=0, square=True, linewidths=.5, cbar_kws={'shrink': .45, 'format': '%.2f'}, vmin=-0.1, annot=True)

    # Do not alter these final lines of code
    fig.savefig('heatmap.png')
    return fig
