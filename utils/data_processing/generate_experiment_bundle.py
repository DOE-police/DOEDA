#!/usr/bin/env python3
from turtle import st
import click
import yaml
import json
import os


@click.command()
@click.option(
    "-p", "--experiments-path", help="Path to the folder containing the experiments."
)
def generate_json_bundle(experiments_path: str):
    try:
        if experiments_path.endswith("/") == False:
            experiments_path += "/"
        experiments = os.listdir(experiments_path)
        experiments_dict = list()
        file_number = 1
        for experiment in experiments:
            with open(experiments_path + experiment, "r") as yaml_doc:
                yaml_to_dict = yaml.load(yaml_doc, Loader=yaml.FullLoader)
                yaml_to_dict["row_number"] = file_number
                experiments_dict.append(yaml_to_dict)
            file_number += 1
        with open("experiments-bundle.json", "w") as json_doc:
            json.dump(experiments_dict, json_doc)
            print("✅ Experiment JSON bundle successfully generated")
    except Exception as e:
        print("❌ Problem occurred, JSON bundle was not generated")
        raise Exception("experiment JSON bundle was not generated")


if __name__ == "__main__":
    generate_json_bundle()
