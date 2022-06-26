import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('online_retail_II.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year']        = pd.DatetimeIndex(df['InvoiceDate']).year

sales = df[ (df['Invoice'].str.contains('C')==False) & (df['Quantity']> 0) ]
sales['Revenue'] = sales['Quantity'] * sales['Price']

sales_year = sales[['Year', 'Revenue']].groupby(['Year']).mean('Revenue')

print(sales_year)

