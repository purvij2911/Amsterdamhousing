import pandas as pd


def read_data():

   header_columns=["area","single","married, no kids","not married, no kids","married, with kids","not married, with kids","single parent","other","total"]
   df = pd.read_excel('data/2021_family_composition_amsterdam.xlsx', engine='openpyxl', skiprows=2, usecols="A:I")
   prices = pd.read_excel('data/woz_prices_2021_amsterdam.xlsx', engine='openpyxl', skiprows=2, usecols="A:B")

   # Remove rows with all null values and drop redundant columns
   prices.dropna(how="all", inplace=True)
   df.dropna(how="all", inplace=True)
   df = df.loc[df["area"] != "ASD Amsterdam"]
   prices = prices.loc[prices["area"] != "ASD Amsterdam"]
   df.drop('total', axis=1, inplace=True)

   # Merge the dataframes on the 'area' column
   df = df.merge(prices, on='area', how='inner')
   
   # Exclude 'area' column when converting other columns to numeric type
   col = ['single', 'married, no kids', 'not married, no kids', 'married, with kids', 'not married, with kids', 'single parent', 'other','average woz value']
   df[col] = df[col].apply(pd.to_numeric, errors='coerce')
   df.fillna(round(df.mean(),2), inplace=True)

   return df

