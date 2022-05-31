#!/usr/bin/env python3
"""
Generate the skeleton of a YAML document, based on the contents of the csv file.

The csv file should:
- contain one row per experimental run
- contain one column per factor
- have its last column as the response
- have its first row containing the variable names

Units: if the variables have units they should be specified at the end of the
variable name between bracket, i.e. 'Distance (m)'.
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
    "--header/--no-header",
    default="--no-header",
    show_default=True,
    help="Variable names are specified in first row of the csv file.",
)
@click.option(
    '--units/--no-units',
    default="--no-units",
    show_default=True,
    help="Units are added between brackets at the end of the variable names."
)
@click.option(
    "--coded/--uncoded",
    default="--uncoded",
    show_default=True,
    help="Factor levels are in coded form.",
)
@click.option(
    "--response",
    default=0,
    type=int,
    show_default=True,
    help="Number of response variables present in the dataset. Set to 0 if no "
         "response variable is provided."
)
@click.option(
    "--title",
    type=str,
    default=None,
    help="Title of the experiment. Filename is used if none is given. Maximum 15 "
         "words. If too long, only first 15 words given are used."
)
@click.option(
    "--doi",
    type=str,
    default=None,
    help="DOI of the experiment or the source of the data. If the full DOI is "
         "'htpps://doi.org/10.1000/xyz123' then the DOI provided must be in the form '10.1000/xyz123'"
)
@click.option(
    "--source",
    type=str,
    default=None,
    help="Reference for the source of the data if the DOI is not available."
)
@click.option(
    "--description",
    type=str,
    default=None,
    help="Description of the experiment. Should contain the overall goal and a quick "
         "description of the variables used. Maximum 250 words. If too long, "
         "only first 15 words given are used."
)
@click.option(
    "-k",
    "--keyword",
    type=str,
    multiple=True,
    default=[],
    help="Keyword defining attributes of the design. Must be specified individually, "
         "each with a '-k' option. All keywords must be single words, or hyphen "
         "separated (i.e. fractional-factorial)."
)
@click.option(
    "--decimal",
    type=str,
    default=",",
    show_default=True,
    help="Separator used for the decimals in the csv file."
)
def main(infile, outfile, header, units, coded, response, title, doi, source,
         description, keyword, decimal):
    """
    Read the contents of the csv file INFILE to generate the skeleton of the experiment
    file. Save the output file to a YAML file named OUTFILE.
    """
    # Options for loading the csv file
    if header:
        header_value = 0
    else:
        header_value = None
    # Loading file to a dataframe to keep column name
    df = pd.read_csv(
        # FIXME problem with the encoding for variables containing greek letters
        infile, header=header_value, index_col=None, encoding="utf-8", sep=";", decimal=decimal
    )
    # Retrieve units from variable names if needed
    var_units = dict()
    if units:
        for col in df.columns:
            units_rgx = re.search(r'\((.+)\)$', col)
            # Check if the regex captured something in the headers
            if units_rgx is None:
                var_units[col] = None
            else:
                var_units[col] = units_rgx.group(1)
    # Only dict are written to yaml
    data_dict = dict()
    # Infer title from filename
    if title is None:
        exp_title = (
            re.search(r"/(\w+)\.csv", infile)
            .group(1)
            .replace("_", " ")
            .replace("-", " ")
        )
    else:
        exp_title = title
    # Only 15 words max
    word_list = exp_title.split()
    if len(word_list) > 15:
        exp_title = ' '.join(word_list[0:15])
    data_dict["title"] = exp_title
    # Run size and n_factors given by the matrix dimensions
    data_dict["run_size"] = df.shape[0]
    # For each variable in df, gather characteristics
    data_dict["dataset"] = []
    if response > 0:
        response_in = True
        data_dict['response'] = []
    else:
        response_in = False
    for factor_index, factor_name in enumerate(df.columns):  # index by column names
        # Check if the factor is a response column or not
        if response_in and (factor_index >= (df.shape[1] - response)):
            factor = {
                "name": factor_name,
                "value": df[factor_name].to_list(),
                "units": var_units.get(factor_name)
            }
            data_dict['response'].append(factor)
        else:
            if coded:
                column = None
                coded_column = df[factor_name].to_list()
                levels = np.unique(coded_column)
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
                "units": var_units.get(factor_name)
            }
            data_dict["dataset"].append(factor)

    # Check if multilevel by comparing the number of factors
    n_levels = [i["levels"] for i in data_dict["dataset"]]
    data_dict["multilevel"] = len(np.unique(n_levels)) > 1
    # DOI of the form '10.1000/xyz123' coming from 'https://doi.org/10.1000/xyz123'
    if doi is not None:
        data_dict["doi"] = doi
    if source is not None:
        data_dict["source"] = source
    
    # Description cannot have more than 250 words, the rest is discarded
    if description is not None:
        desc_word_list = description.split()
        if len(desc_word_list) > 250:
            description = ' '.join(desc_word_list[0:250])
    data_dict["description"] = description
    # For now keywords is not infered from the file
    data_dict["keywords"] = [i.lower() for i in keyword]
    # Save experiment data to yaml file, use filename as path
    try:
        with open(outfile, "w") as file:
            yaml.dump(
                data_dict,
                file,
                default_flow_style=False,
                sort_keys=False,
                indent=2,
                allow_unicode=True,
                encoding="utf-8",
            )
        print("Csv successfully converted to yaml! 👍")
    except Exception as e:
        print("Writing csv to yaml failed!\n%s" % str(e))
        exit(1)


if __name__ == "__main__":
    main()
