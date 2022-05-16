# DOEDA

**D**esign **o**f **E**xepriments **Da**tabase, or DOEDA, is a database that gathers information about experiments that were perfomed using an experimental design.
The main goal of DOEDA is to provide a central interface to easily acess all experiments.

## Information about experiments

For each experiment, the database provides the following information:

- **Title**: A short description of the experiment.
- **Run size**: The number of experimental runs.
- **Keywords**: a list of keywords to identify the main attributes of the experiment. For the full list of keywords, see the "Attributes" section below.
- **Data**: actual dataset of the experiment.
- **Documentation**: a more detailed description of the experiment and the variables used.
- **Reference**: a DOI string to identify the source of the data

## Experiment attributes

Experiment attributes are keywords that describe the speicifities of the experimental design used in the experiment.
A list of all possible experiment attributes is available in the [glossary](docs/glossary.md)

## Data and file conventions

<!-- TODO: explain the structure needed in the datafile -->

## Utility scripts

A few utility scripts are available in the `utils\` folder.
Their usage are explained with examples in [this](docs/example.md) section.
