import pandas as pd
import matplotlib.pyplot as plt

order = pd.read_csv('order_details.csv', parse_dates=['order_date','order_time'])
menu = pd.read_csv('menu_items.csv')

# Join columns

order['order_datetime'] = pd.to_datetime(order['order_date'].astype(str) + ' ' + order['order_time'].astype(str))
order = order.drop(columns=['order_date', 'order_time'])

# Cleaning null values

order = order.dropna()

# Join data

order_items = order.merge(menu, how='left', left_on='item_id', right_on='menu_item_id').drop('menu_item_id', axis=1)

# Add columns 

order_items['sales_taxes'] = (order_items.price * 0.08).round(2)
order_items['total_revenue'] = (order_items.price + order_items.sales_taxes).round(2)
order_items['weekday'] = order_items.order_datetime.dt.day_of_week

busiest_time = order_items.groupby('weekday')['total_revenue'].sum()

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

busiest_time.plot(kind='bar', figsize=(10, 6), width=0.5)

plt.xticks(ticks=range(7), labels=days_of_week, rotation=45)
plt.xlabel('Day of the Week')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Weekday')

plt.tight_layout()
plt.show()