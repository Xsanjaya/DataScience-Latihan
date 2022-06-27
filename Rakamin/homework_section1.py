import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('online_retail_II.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year']        = pd.DatetimeIndex(df['InvoiceDate']).year

sales = df[ (df['Invoice'].str.contains('C')==False) & (df['Quantity']> 0) ]
sales['Revenue'] = sales['Quantity'] * sales['Price']

sales_year = sales[['Year', 'Revenue']].groupby(['Year']).mean()

sales_year.plot(kind='bar', title='Revenue per Year', ylabel='Revenue (£)',
         xlabel='Year', figsize=(7, 6))
plt.show()

print(sales_year)
# print(sales_year.info())

