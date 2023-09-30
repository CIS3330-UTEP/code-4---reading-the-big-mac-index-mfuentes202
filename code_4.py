import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year, country_code):
    filtered_df = df.query(f'date == {year} and iso_a3.str.lower() == "{country_code.lower()}"')
    mean_dollar_price = round(filtered_df['dollar_price'].mean(), 2)
    return mean_dollar_price

def get_big_mac_price_by_country(country_code):
    filtered_df = df.query(f'iso_a3.str.lower() == "{country_code.lower()}"')
    mean_dollar_price = round(filtered_df['dollar_price'].mean(), 2)
    return mean_dollar_price

def get_the_cheapest_big_mac_price_by_year(year):
    min_price_row = df[df['date'] == year].nsmallest(1, 'dollar_price').iloc[0]
    country_name = min_price_row['name']
    iso_a3 = min_price_row['iso_a3']
    dollar_price = min_price_row['dollar_price']
    return f'{country_name}({iso_a3}): ${dollar_price}'

def get_the_most_expensive_big_mac_price_by_year(year):
    max_price_row = df[df['date'] == year].nlargest(1, 'dollar_price').iloc[0]
    country_name = max_price_row['name']
    iso_a3 = max_price_row['iso_a3']
    dollar_price = max_price_row['dollar_price']
    return f'{country_name}({iso_a3}): ${dollar_price}'

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010, "arg")
    print(f'Mean Big Mac Price in 2010 for Argentina: {result_a}')
    
    result_b = get_big_mac_price_by_country("arg")
    print(f'Mean Big Mac Price for Argentina: {result_b}')
    
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(f'The Cheapest Big Mac in 2008: {result_c}')
    
    result_d = get_the_most_expensive_big_mac_price_by_year(2003)
    print(f'The Most Expensive Big Mac in 2003: {result_d}')
