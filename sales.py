import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\chris\workbench\Final-Assignment\sales_2016_2019.csv')

# calculate sales bottles sold wise
df1 = df.groupby(['zip_code', 'item_number']).agg({'bottles_sold':'sum'}).reset_index()
print('\nCALCULATION OF BOTTLE SALES PER ZIP CODE:\n',df)


# sorted list of sales
print('\nLIST OF TOP SELLING ITEMS DESENDING:\n',df1.sort_values(by='bottles_sold', ascending=False))


# top 5 of bottles sold   
top5 = df1.sort_values(by='bottles_sold', ascending=False).head(5)

# convert the top 5 sales to np array    
top5 = np.array(top5['bottles_sold'])


colors = np.random.rand(len(df1['item_number']))

# plot scatter
plt.figure(figsize=(12,6))
plt.scatter(df1.index, df1['bottles_sold'], c=colors)
for i, item in enumerate(df1['item_number']):
    if df1['bottles_sold'][i] in top5:
        plt.annotate(item, (df1.index[i], df1['bottles_sold'][i]))
plt.xlabel('Zipcode')
plt.ylabel('Bottles Sold')
plt.title('Bottles sold')
plt.show()


# calculate dollar sales per store name

dollars = df.groupby('store_name').agg({'sale_dollars':'sum'}).reset_index()
# calculate percentage of sales per store
dollars['percentage'] = (dollars['sale_dollars']/dollars['sale_dollars'].sum())*100
dollars_sort = dollars.sort_values(by='percentage')
dollars_sort = dollars_sort.round(2)
print('\nSTORE SALES IN DOLLARS AND PERCENTAGE:\n', dollars_sort.sort_values(by='percentage', ascending=False))

#plot horizontal bar graph
plt.figure(figsize=(24,6))
plt.barh(dollars_sort['store_name'][-15:], dollars_sort['percentage'][-15:])
for i, v in enumerate(dollars_sort['percentage'][-15:]):
    plt.annotate(str(v), (v,i), textcoords="offset points", xytext=(5,-5), ha='left')
plt.xlabel('%Sales')
plt.title('%Sales by store')
plt.show()