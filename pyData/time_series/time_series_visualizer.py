import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data and parse dates. Also, set the index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
# Filter the data for when the page views are in the top 2.5% or the bottom 2.5%
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Utilise this function to create a line chart using Matplotlib
    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
    # Set the title as well as the axes to the correct names
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Data')
    ax.set_ylabel('Page Views')
    # Draw the line plot of the data frame
    sns.lineplot(data=df, legend=False)

    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()
    df_bar = pd.DataFrame(df_bar.groupby(['Years', 'Months'], sort=False)[
                          'value'].mean().round().astype(int))
    df_bar = df_bar.rename(columns={'value': 'Average Page Views'})
    df_bar = df_bar.reset_index()
    missing_data = {
        'Years': [2016, 2016, 2016, 2016],
        'Months': ['January', 'February', 'March', 'April'],
        'Average Page Views': [0, 0, 0, 0]
    }

    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])
    # Draw bar plot using matplotlib and seaborn methods
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_title('Daily freeCodeCamp Forum Average Page Views per Month')

    bar_chart = sns.barplot(
        data=df_bar, x='Years', y='Average Page Views', hue='Months', palette='tab10')
    bar_chart.set_xticklabels(bar_chart.get_xticklabels(
    ), rotation=90, horizontalalignment='center')

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Data which will be used for the box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Make use of Seaborn methods to create the box plots ->
    fig, axes = plt.subplots(1, 2, figsize=(32, 10), dpi=100)

    # Our year-wise box plot
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Our month-wise box plot
    mnths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=mnths, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Months')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
