import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import null

df = pd.read_csv('online_retail_II.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year']        = pd.DatetimeIndex(df['InvoiceDate']).year

sales = df[ (df['Invoice'].str.contains('C')==False) & (df['Quantity']> 0) ]
sales.assign(Revenue = sales['Quantity'] * sales['Price'])

sales_year = sales[['Year', 'Revenue']].groupby(['Year']).mean()

finished = sales[ sales['Customer ID'].notnull() ]
cancel 	= df[ (df['Invoice'].str.contains('C')==True)]

df_akhir = pd.concat([finished, cancel])
df_akhir['is_success'] = df_akhir['Invoice'].str.contains('C')==False
# df_akhir_years = df_akhir[['Year', 'is_success', 'Invoice']].groupby(['Year','is_success']).count()

print(df_akhir)

