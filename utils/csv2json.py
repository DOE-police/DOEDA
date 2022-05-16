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
    "--title",
    type=str,
    default=None,
    help="Title of the experiment. Filename is used if none is given. Maximum 15 "
         "words. If too long, only first 15 words given are used.",
)
@click.option(
    "--doi",
    type=str,
    default=None,
    help="DOI of the experiment or the source of the data. Should be in the form "
         "'htpps://doi.org/10.1000/xyz123' or be a valid URL.",
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
# TODO: add option to specify the repsonse (if any) and the number of repsonse variables
def main(infile, outfile, header, units, coded, title, doi, description, keyword):
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
        infile, header=header_value, index_col=None, encoding="windows-1252", sep=";"
    )
    # Retrieve units from variable names if needed
    if units:
        var_units = dict()
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
            "units": var_units.get(factor_name)
        }
        data_dict["design"].append(factor)
    # Check if multilevel by comparing the number of factors
    n_levels = [i["levels"] for i in data_dict["design"]]
    data_dict["multilevel"] = len(np.unique(n_levels)) > 1
    # DOI of the form https://doi.org/10.1000/xyz123
    data_dict['doi'] = doi
    # Description cannot have more than 250 words, the rest is discarded
    if description is not None:
        desc_word_list = description.split()
        if len(desc_word_list) > 250:
            description = ' '.join(desc_word_list[0:250])
    data_dict["description"] = description
    # For now keywords is not infered from the file
    data_dict["keywords"] = [i.lower() for i in keyword]
    # Save experiment data to yaml file, use filename as path
    with open(outfile, "w") as file:
        yaml.dump(
            data_dict,
            file,
            default_flow_style=True,
            sort_keys=False,
            indent=2,
            allow_unicode=True,
            encoding="latin1",
        )


if __name__ == "__main__":
    main()
