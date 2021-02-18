import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df.date = pd.to_datetime(df.date, format='%Y-%m-%d')
df = df.set_index('date')

# Clean data
df = df.loc[(df['value'] <= df['value'].quantile(0.975)) &
            (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df['value'], label='Línea 1', linewidth=4, color='red')
    ax.set(xlabel='Date', ylabel='Page Views',
           title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)

    df_bar['Years'] = pd.DatetimeIndex(df_bar.date).year

    df_bar['Months'] = pd.DatetimeIndex(df_bar.date).month

    df_bar = df_bar.sort_values(by=['Months'])

    df_bar['Months'] = pd.DatetimeIndex(df_bar.date).month_name()
    # Draw bar plot
    fig, ax = plt.subplots()
    g = sns.catplot(x="Years", y="value", palette="bright",
                    ci=None, hue="Months", kind="bar", legend=False, data=df_bar)
    g.set(xlabel='Years', ylabel='Average Page Views')
    plt.legend(loc='upper left')
    g.set_xticklabels(rotation=90)
    fig = g.fig    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_order'] = pd.DatetimeIndex(df_box.date).month
    df_box = df_box.sort_values(by=['month_order', 'year'])

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1 = sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    ax2 = sns.boxplot(x="month", y="value", data=df_box, ax=ax2)
    ax1.set(xlabel="Year", ylabel="Page Views")
    ax2.set(xlabel="Month", ylabel="Page Views")
    ax1.set(title='Year-wise Box Plot (Trend)')
    ax2.set(title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
