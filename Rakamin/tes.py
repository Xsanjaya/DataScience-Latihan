import pandas as pd

df = pd.read_csv('insurance.csv')

df = df[(df['sex']=='male') & (df['smoker']=='yes') & (df['age']>50)]
df['new_bmi'] = df['bmi']-1.5

print(df['new_bmi'].mean())