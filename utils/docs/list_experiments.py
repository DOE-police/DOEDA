"""
Retrieve the description of all experiments and generate a list for the documentation.
"""

import glob
import yaml
from typing import List

# TODO: these changes are hard-coded and their should be a global rule for all keywords
def reformat_kw(kw: str) -> str:
    if kw == "dsd":
        return "DSD"
    out = kw.replace("-", " ").title()
    if kw == "plackett-burman":
        out = out.replace(" ", "-")
    return out


def main(dir_path: str) -> List[str]:
    exp_files_list = glob.glob(f"{dir_path}/*.yaml")
    names = []
    descriptions = []
    keywords = []
    for exp_file in exp_files_list:
        with open(exp_file, "r") as file:
            experiment_list = yaml.full_load(file)
            names.append(experiment_list.get("title"))
            descriptions.append(experiment_list.get("description"))
            keywords.append(experiment_list.get("keywords"))
    return names, descriptions, keywords


if __name__ == "__main__":
    try:
        names_list, desc_list, kw_list = main("experiments")
        outpath = "docs/source/experiment_list.rst"
        with open(outpath, "w") as f:
            # Label
            f.write(".. _experiment-list:\n\n")
            # Title
            f.write("List of experiments\n===================\n\n")
            # Glossary procedure
            f.write(".. glossary::\n  :sorted:\n\n")
            # Write all details
            for i, name in enumerate(names_list):
                desc = desc_list[i]
                # Title and description
                f.write(f"  {name}:\n    {desc}\n\n")
                # Keywords
                formatted_kw = [f":term:`{reformat_kw(kw)}`" for kw in kw_list[i]]
                f.write(f'    *Keywords*: {", ".join(formatted_kw)}\n')
                # final newline
                f.write("\n")
        print("👍 All experiments listed in %s" % outpath)
    except Exception as e:
        print("⚠ Could not list all the experiments ! %s" % str(e))
        exit(1)
