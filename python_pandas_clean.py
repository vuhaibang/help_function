import pandas as pd
df = pd.DataFrame({'province': ['A', 'B', 'C', 'D'],
                  'money': [1,4,2,6],
                  'distance': [1,3,4,5]})

# Apply format
format = lambda x: '%.2f' % x
df[['money', 'distance']] = df[['money', 'distance']].applymap(format)
# df['money'] = df['money'].map(format)

# pivot table


# Melt table

# Sum

# Replace

countries_dict = {'A': 'a', 'B': 'b'}
df['country'].replace(countries_dict, inplace=True)

df['country'].str.replace(",", " ")