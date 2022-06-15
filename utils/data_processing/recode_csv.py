"""
Recode the levels of the factors in a csv file.
"""
import json
import click
import pandas as pd


@click.command()
@click.option('-f',
              '--filepath',
              type=str,
              required=True,
              help='Path of the file to recode')
@click.option('-l',
              '--levels-filepath',
              type=str,
              required=True,
              help="Path of the JSON file containing the new levels.")
def main(filepath, levels_filepath, sep=";", decimal=","):
    """
    Recode the levels of one or several columns in a CSV file using a levels-recoding file.

    The levels-recoding file is a JSON file with an array containing one element per
    column to recode.
    Each element contains two fields:
    - "index": the index (0-based) of the column to recode in the csv file.
    - "map": a map of the value to recode. This map contains itself one field per
    level to recode in the column, written in pairs {"old": new}

    For example, if we want to recode the third column of our csv file in the
    following way: -1 to 0, 0 to 100 and 1 to 200, the levels-recoding JSON file
    will be:

    [{"index": 2,"map": {"-1": 0, "0": 100, "1": 200}}]
    """
    try:
        with open(levels_filepath) as f:
            levels_eq = json.load(f)
    except Exception as e:
        print('Could not read the JSON file containing the new levels. %s' % e)
        exit(1)
    # Load the csv file
    try:
        df = pd.read_csv(filepath, sep=sep, decimal=decimal)
    except Exception as e:
        print('Could not open the CSV file. %s' % e)
        exit(1)
    # Recode the variables
    columns = df.columns
    for level in levels_eq:
        col = columns[level.get("index")]
        col_map = {int(k): v for k, v in level.get("map").items()}
        df[col] = df[col].map(col_map)
    # Save the new df to csv file
    new_path = filepath.replace(".csv", "_recoded.csv")
    df.to_csv(new_path, sep=sep, decimal=decimal, index=False)
    print('CSV sucessfully recoded.')
    exit(0)


if __name__ == "__main__":
    main()
