"""
Generate the skeleton of a JSON document, based on the contents of the csv file.

The csv file should:
- contain one row per experimental run
- contain one column per factor
- have its last column as the response
- have its first row contain the variable names
"""
import re

import yaml

import click
import numpy as np
import pandas as pd


@click.command()
@click.argument("infile")
@click.argument("outfile")
@click.option(
    "--no-header",
    default=False,
    is_flag=True,
    show_default=True,
    help="Flag. Variable names are not in first row of csv file.",
)
@click.option(
    "--coded",
    default=False,
    is_flag=True,
    show_default=True,
    help="Flag. Factor levels are in coded form.",
)
@click.option(
    "-t",
    "--title",
    type=str,
    default=None,
    help="Title of the experiment. Filename is used if none is given.",
)
# TODO: add option to specify the repsonse (if any) and the number of repsonse variables
# TODO: add an option to submit the DOI (+ check to remove the 'htpps://doi.org/'
#  from the string if it is there)
def main(infile, outfile, no_header, coded, title):
    """
    Read the contents of the csv file INFILE to generate the skeleton experiment file.
    Save the output file to a YAML file OUTFILE.
    """
    # Options for loading the csv file
    if no_header:
        header = None
    else:
        header = 0
    # Loading file to a dataframe to keep column name
    df = pd.read_csv(infile, header=header, index_col=None, encoding='windows-1252',
                     sep=';')
    # Only dict are written to yaml
    data_dict = dict()
    # Infer title from filename
    if title is None:
        exp_title = re.search(r'\/(\w+)\.csv', infile).group(1).replace("_",
                                                                        " ").replace(
            "-", " ")
    else:
        exp_title = title
    data_dict["title"] = exp_title
    # Run size and n_factors given by the matrix dimensions
    data_dict["runsize"] = df.shape[0]
    # For each variable in df, gather characteristics
    data_dict["design"] = []
    for factor_name in df.columns:  # index by column names
        if coded:
            column = None
            coded_column = df[factor_name].to_list()
            levels = np.unique(column)
        else:
            column = df[factor_name].to_list()
            levels = np.unique(column)
            # Rule for recoding the factor levels
            rule = dict()
            for i, x in enumerate(levels):
                # Levels are -1, 0, 1 if it's a three-level factor
                idx = i - 1 if len(levels) == 3 else i
                rule[x] = idx
            # Recode the column
            coded_column = [rule[x] for x in column]
        factor = {
            "name": factor_name,
            "uncoded": column,
            "coded": coded_column,
            "levels": len(levels),
            "units": "NA",
        }
        data_dict["design"].append(factor)
    # Check if multilevel by comparing the number of factors
    n_levels = [i["levels"] for i in data_dict["design"]]
    data_dict["multilevel"] = len(np.unique(n_levels)) > 1
    # For now, description, keywords and DOI are not infered from the file
    data_dict["description"] = None
    data_dict["keywords"] = []
    data_dict["doi"] = None
    # Save experiment data to yaml file, use filename as path
    with open(outfile, "w") as file:
        yaml.dump(data_dict, file, default_flow_style=True, sort_keys=False,
                  indent=4, allow_unicode=True, encoding='windows-1252')


if __name__ == "__main__":
    main()
