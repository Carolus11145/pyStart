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
    lambda x: 0 if x == 0 else 1)  # Normalises the cholesterol data set
# Normalises the glucose data set
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 0 else 1)

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

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None

    # 14
    fig, ax = None

    # 15

    # 16
    fig.savefig('heatmap.png')
    return fig
