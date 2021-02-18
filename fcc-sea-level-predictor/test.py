import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df.Year, df['CSIRO Adjusted Sea Level'])
    plt.plot(df.Year, intercept + slope*df.Year, 'r', label='fitted line')
    # Create second line of best fit

    recent = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(
        recent.Year, recent['CSIRO Adjusted Sea Level'])
    years = pd.Series(list(range(1880, 2051)))
    plt.plot(years, intercept + slope*years, 'r', label='fitted line')
    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
