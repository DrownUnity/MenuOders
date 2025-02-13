import pandas as pd
import matplotlib.pyplot as plt

order = pd.read_csv('order_details.csv', parse_dates=['order_date','order_time'])
menu = pd.read_csv('menu_items.csv')

# Cleaning null values

order = order.dropna()

# Join data

order_items = order.merge(menu, how='left', left_on='item_id', right_on='menu_item_id').drop('menu_item_id', axis=1)

# Add columns 

order_items['sales_taxes'] = (order_items.price * 0.08).round(2)
order_items['total_revenue'] = (order_items.price + order_items.sales_taxes).round(2)

#Group and sort

order_items_grouped = (
    order_items
    .groupby("item_name")
    .agg({'total_revenue': 'sum'})
    .sort_values(by='total_revenue'))

# Graph

order_items_grouped.plot(kind='barh', y='total_revenue')

# Category analysis 

order_items_grouped_category = (
    order_items
    .groupby("category")
    .agg({'total_revenue': 'sum'})
    .sort_values(by='total_revenue'))

order_items_grouped_category.plot(kind='barh', y='total_revenue')

# Asian

asian_items = order_items[order_items['category'] == 'Asian']

asian_items_grouped = (
    asian_items
    .groupby("item_name")
    .agg({'total_revenue': 'sum'})
    .sort_values(by='total_revenue')
)

asian_items_grouped.plot(kind='barh', figsize=(10, 6))

# Mexican

mexican_items = order_items[order_items['category'] == 'Mexican']

mexican_items_grouped = (
    mexican_items
    .groupby("item_name")
    .agg({'total_revenue': 'sum'})
    .sort_values(by='total_revenue'))

mexican_items_grouped.plot(kind='barh', figsize=(10, 6))

# Italian 

italian_items = order_items[order_items['category'] == 'Italian']
italian_items_grouped = (
    italian_items
    .groupby("item_name")
    .agg({'total_revenue': 'sum'})
    .sort_values(by='total_revenue')
)
italian_items_grouped.plot(kind='barh', figsize=(10, 6))


# American 

american_items = order_items[order_items['category'] == 'American']
american_items_grouped = (
    american_items
    .groupby("item_name")
    .agg({'total_revenue': 'sum'})
    .sort_values(by='total_revenue')
)
american_items_grouped.plot(kind='barh', figsize=(10, 6))

print(plt.show())