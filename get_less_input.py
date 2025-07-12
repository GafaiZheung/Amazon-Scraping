import pandas as pd

df = pd.read_csv('input.csv')

#获取国家列表
countries = df['country'].unique().tolist()

#每个国家抽10个组成新的df
new_df = df[df['country'].isin(countries)].groupby('country').apply(lambda x: x.sample(n=10, random_state=42)).reset_index(drop=True)

new_df.to_csv('input_less.csv', index=False)
