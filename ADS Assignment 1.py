import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot line graph for annual % growth of exports of goods and service for selected countries


def line(x):
    
 
    '''
    Plots a line graph for annual % growth of exports of goods & service for 
    selected countries.

    Args:
    x: pandas dataframe containing data for selected countries and years.

    '''
    
    plt.figure(figsize=(30, 16.5))
    # Defining the list of selected countries and years
    x = x.head(12)
    countries = ['Australia', 'Brazil', 'France', 'Germany', 'India', 'Indonesia', 
                 'Italy', 'Japan', 'Korea', 'Mexico', 'Netherlands','Russian',
                 'Spain', 'Switzerland', 'United Kingdom', 'United States',
                 'Canada', 'Ireland', 'New Zealand']
    years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', 
             '2018', '2019', '2020', '2021']

    for country in countries:
            # Plotting the line graph for each country
        plt.plot(years, x[country], label=country, marker='*')
    plt.xlabel("Year", fontsize=15, fontweight='bold')
    plt.ylabel('% Growth',fontsize=15, fontweight='bold')
    plt.title("Export of goods and service annual growth percentage", 
              fontweight = 'bold')
    plt.legend(bbox_to_anchor=(0.6,0.5), facecolor='pink', framealpha=0.5,
               fontsize='x-large')
    plt.savefig('line_plot.png')
    plt.show()
    
    return

# Loading the data for the line graph
export_data = pd.read_excel(r'C:\Users\Diraj\Downloads\Masters - DS\Applied DS- 1\exports_good_service(annual%growth).xlsx')



# Calling the line function with the loaded data
line(export_data)

# Function to plot horizontal bar chart for top 20 batsman's

def top_batsman(a):
    
    
    '''
    Plots a horizontal bar chart for top 20 batsmen high rated batsman with the
    most half-century and century scores.

    Args:
    a: pandas dataframe containing data for top 100 batsmen and their ratings,
    runs,matches played , innings,high scores, half-century scores and century
    scores.
    
    '''
    # Sorting the data by rating in descending order
    a = a.sort_values('rating', ascending=False)
    
    plt.figure(figsize=(15, 10))
    # Plotting the horizontal bar chart for the top 20 batsmen with most half-century and century 
    plt.barh(a['batsman'].head(20), a['half_century'].head(20), color='plum',
             edgecolor = 'black', joinstyle='miter', label='Half Century')
    plt.barh(a['batsman'].head(20), a['century'].head(20), color ='ivory', 
             edgecolor='black', hatch='.', joinstyle='bevel', 
             label='Century')
    plt.xlabel("Count of half century and century", fontsize=15, 
               fontweight='bold')
    plt.ylabel("Batsman", fontsize=15, fontweight='bold')
    plt.title('Top 20 high rated batsmans with most half century and century',
              fontweight ='bold')
    plt.legend(loc='upper right', facecolor='pink', framealpha=0.5, 
               fontsize='x-large')
    plt.savefig('bar_plot.png')
    plt.show()
    
    return

# Loading the data for the horizontal bar chart
batsman = pd.read_csv('C:/Users/Diraj/Downloads/Masters - DS/Applied DS- 1/topbatsman.csv')


# Calling the top_batsman function with the loaded data
top_batsman(batsman)

# Function to plot scatter plot for batsmen with good strike rate and average

def batsman_average(x):
    
    
    '''
    Plots a scatter plot for batsmen based on their innings played, strike rate
    and average.

    Args:
    x: pandas dataframe containing data for top 100 batsmen and their ratings,
    runs,matches played ,
    innings,high scores, half-century scores and century scores.
    
    '''
    plt.figure(figsize=(15, 8))
    ##plotting a scatter plot for strike rate and average based on their innings
    plt.scatter(x['innings'], x['strike_rate'], s = x['high_score'], marker='^',
                label='Strike Rate', alpha=0.8, c='hotpink', edgecolors='black')
    plt.scatter(x['innings'], x['average'], s = x['high_score'], marker ='o', 
                label='Average',
                alpha=0.8, c ='mediumturquoise', edgecolors='black')
    plt.xlabel('Innings Played', fontsize=10, fontweight ='bold')
    plt.ylabel('Strike Rate & Average', fontsize=10, fontweight ='bold')
    plt.title('Strike Rate and Average based on the total innings they played',
              fontweight='bold')
    plt.legend(loc='upper right', facecolor='pink', framealpha=0.5,
               fontsize='x-large')
    plt.savefig('scatter_plot.png')
    plt.show()
    
    return

# Calling the batsman_average function with the loaded data
batsman_average(batsman)
