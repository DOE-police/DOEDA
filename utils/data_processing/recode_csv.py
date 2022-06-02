"""
Recode the levels of the factors in a csv file.
"""
from typing import List, Dict
import pandas as pd


def main(path: str, levels_eq: List[Dict], sep=';', decimal=','):
    # Load the csv file
    df = pd.read_csv(filepath, sep=sep, decimal=decimal)
    # Recode the variables
    columns = df.columns
    for level in levels_eq:
        col = columns[level.get('index')]
        df[col] = df[col].map(level.get('map'))
    # Save the new df to csv file
    new_path = path.replace('.csv', '_recoded.csv')
    df.to_csv(new_path, sep=sep, decimal=decimal, index=False)


if __name__ == "__main__":
    filepath = 'csv/polyethylene_film.csv'
    levels_recoding = [
        {'index': 1,
         'map': {-1: 0, 0: 200, 1: 400}},
        {'index': 2,
         'map': {-1: 0, 0: 500, 1: 1000}},
        {'index': 3,
         'map': {-1: 0, 0: 500, 1: 1000}},
        {'index': 4,
         'map': {-1: 0, 0: 1000, 1: 2000}},
        {'index': 5,
         'map': {-1: 0, 0: 400, 1: 800}},
    ]
    try:
        main(filepath, levels_recoding)
        print('CSV sucessfully recoded.')
    except Exception as e:
        print(f'Could not recode csv file. {e}')
