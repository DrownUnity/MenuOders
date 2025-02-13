import pandas as pd
import matplotlib.pyplot as plt

order = pd.read_csv('order_details.csv', parse_dates=['order_date'])
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

print(plt.show())