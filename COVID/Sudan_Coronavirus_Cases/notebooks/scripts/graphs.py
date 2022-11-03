import os
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from textwrap import wrap
from matplotlib import ticker

    
def PlotLine(df, column, figsize=(10,6)):
    """
    Plot a line graph using matplotlib 
    -Arguments:
        df: the data frame 
        column: x-axis data
        figsize: figure size to make chart small or big  
    -Returns:
        None
    """
    fig, ax = plt.subplots(figsize=figsize)
    line_data = df[column].value_counts().reset_index().sort_values(by='index')
    line_data['The cumulative occurrence frequency'] = line_data[column].cumsum()
    line_data.plot(x='index', y=column, style='o-', ax=ax, label='Daily Infection')
    line_data.plot(x='index', y='The cumulative occurrence frequency', style='ro-', ax=ax)
    plt.xticks(rotation=90)
    plt.xlabel('')
    
def PieChart(df, column):
    """
    Plot a pie chart using matplotlib 
    -Arguments:
        df: the data frame 
        column: x-axis data
    -Returns:
        None
    """
    
    X = df[column].value_counts()
    plt.pie(X.values, labels=X.index)
    plt.axis('equal')
    plt.show()

def BarChart(df, x, y, label, sort, figsize=(13, 9), ascending=True):
    """
    Bar chart using seaborn 
    -Argumentss:
        df: dataframe 
        x: x-axis column 
        y: y-axis column
        label: string to label the graph
        figsize: figure size to make chart small or big
        ascending: ascending order from smallest to biggest
        sort: which column to sort by 
        
    -Returns:
        None
    """
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.barplot(x=x, y=y, data=df.sort_values(sort, ascending=ascending),
            label=label, color="b", palette=["#0088c0"])
    
    total = df[y].sum()
    for p in ax.patches:
        ax.annotate(str(format(p.get_height()/total * 100, '.2f')) + '%' + ' (' + str(int(p.get_height())) + ')', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 10), textcoords = 'offset points')
    
    y_value=['{:,.0f}'.format(x/total * 100) + '%' for x in ax.get_yticks()]
    plt.yticks(list(plt.yticks()[0]) + [10])
    ax.set_yticklabels(y_value)
    plt.xlabel('')
    plt.ylabel('')
    sns.despine(left=True, bottom=True)