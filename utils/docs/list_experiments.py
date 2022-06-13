"""
Retrieve the description of all experiments and generate a list for the documentation.
"""

import glob
import yaml


def main(dir_path: str):
    exp_files_list = glob.glob(f'{dir_path}\*.yaml')
    names = []
    descriptions = []
    for exp_file in exp_files_list:
        with open(exp_file, 'r') as file:
            experiment_list = yaml.full_load(file)
            names.append(experiment_list.get('title'))
            descriptions.append(experiment_list.get('description'))
    return names, descriptions


if __name__ == "__main__":
    try:
        names_list, desc_list = main('experiments')
        outpath = 'docs/source/experiment_list.rst'
        with open(outpath, 'w') as f:
            # Title
            f.write('List of experiments\n===================\n\n')
            # Glossary procedure
            f.write('.. glossary::\n  :sorted:\n\n')
            for i, name in enumerate(names_list):
                desc = desc_list[i]
                f.write(f'  {name}:\n    {desc}\n\n')
        print('👍 All experiments listed in %s' % outpath)
    except Error as e:
        raise ('Could not list all the experiments ! %s' % e)
