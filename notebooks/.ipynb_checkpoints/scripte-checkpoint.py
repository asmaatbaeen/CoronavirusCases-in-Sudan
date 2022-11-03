def PlotLine(df,x_data, figsize=(16,8)):
    
    """
    Plot a line graph using matplotlib 
    -Arguments:
        df: the data frame 
        x_data: x-axis data
        figsize: figure size to make chart small or big  
    -Return:
        Nothing just show the graph
    """
    sns.set_style("whitegrid")
    sns.set_context("paper", font_scale=2)
    fig, ax = plt.subplots(figsize=figsize)
    data = df[x_data].value_counts().reset_index().sort_values(by='index')
    data['DataCount'] = data[x_data].cumsum()
    ax = sns.lineplot(x='index', y="DataCount", data=data,linewidth=2.5
        ,color=sns.xkcd_rgb['windows blue'],ax=ax,label='Infection Over Time',marker="<")
    ax = sns.lineplot(x='index', y=x_data, data=data,linewidth=2.5
                     , color="coral", ax=ax,label='Daily Infection',marker="<")
    plt.xticks(rotation=90)
    plt.ylabel('')
    plt.xlabel('')
    #ax.set(xticks=df.Date[2::2])
    sns.despine(left=True)
    plt.tight_layout()
    #plt.savefig('PlotLine.pdf', format='pdf', dpi=1200)

def PlotLine1(df,x_data, figsize=(16,8)):
    
    """
    Plot a line graph using matplotlib 
    -Arguments:
        df: the data frame 
        x_data: x-axis data
        figsize: figure size to make chart small or big  
    -Return:
        Nothing just show the graph
    """
    sns.set_style("whitegrid")
    sns.set_context("paper", font_scale=2)
    fig, ax = plt.subplots(figsize=figsize)
    data = df[x_data].value_counts().reset_index().sort_values(by='index')
    data['DataCount'] = data[x_data].cumsum()
    ax = sns.lineplot(x='DataCount', y="DataCount", data=data,linewidth=2.5
        ,color=sns.xkcd_rgb['windows blue'],ax=ax,label='Infection Over Time',marker="<")
    plt.xticks(rotation=90)
    plt.ylabel('')
    plt.xlabel('')
    #ax.set(xticks=df.Date[2::2])
    sns.despine(left=True)
    plt.tight_layout()
    #plt.savefig('PlotLine.pdf', format='pdf', dpi=1200)
    

def BarChart(df,x_data,y_data, figsize=(10,4)):
    
    """
    Bar chart using seaborn 
    -Argumentss:
        df: the data frame 
        x_data: x-axis data 
        y_data: y-axis data
        figsize: figure size
    -Returns:
        Nothing just show the graph
    """
    sns.set_style("whitegrid")
    sns.set_context("paper", font_scale=2)

    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.barplot(x=x_data, y=y_data, data=df,linewidth=1.5,
                     color=sns.xkcd_rgb['windows blue'], edgecolor=".3")
    Sum = df.values[:,1].sum()
    for i,j in enumerate(df.values[:, 1]):
        ax.text(j + 0.01, i + .20,'('+ str(j) + ')Cases')
    plt.ylabel('')
    plt.xlabel('')
    labels = [ '\n'.join(wrap(k,10)) for k in df.values[:, 0]]
    x_value=['{:,.0f}'.format(x/Sum * 100) + '%' for x in ax.get_xticks()]
    ax.set_yticklabels(labels,fontsize=15)
    plt.xticks(list(plt.xticks()[0]))
    ax.set_xticklabels(x_value,fontsize=15)
    sns.despine(left=True)
    #ax.axes.set_title("COVID-19 Patients: Travelers vs Local Transmission",fontsize=20)
    plt.tight_layout()
    #plt.savefig('BarChart.pdf', format='pdf', dpi=1200)

    
def PieChart(df,x_data,figsize=(7, 5)):
    
    """
    Plot a pie chart using matplotlib 
    -Arguments:
        df: the data frame 
        x_data: x-axis data
    -Return:
        Nothing just show the graph
    """
    fig, ax = plt.subplots(figsize=figsize)


    explode=(0,0.1,0,0,0)
    Theme = plt.get_cmap('copper')
    
    X = df[x_data].value_counts()
    ax.set_prop_cycle("color", [Theme(1. * i / len(X.values))
                             for i in range(len(X.values))])

    my_circle=plt.Circle( (0,0), 0.6, color='white')
    plt.pie(X.values, labels=None,explode=explode)
    plt.gca().add_artist(my_circle)
    plt.legend(bbox_to_anchor=(0.95,.95), loc=2, borderaxespad=0,labels=X.index)
    plt.axis('equal')
    plt.tight_layout()
    #plt.savefig('PieChart.pdf', format='pdf', dpi=1200)
    plt.show()
