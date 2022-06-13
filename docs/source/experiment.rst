Information about experiments
=============================

For each experiment, the database provides the following information:

- **Title**: A short description of the experiment.
- **Run size**: The number of experimental runs.
- **Design**: actual dataset of the experiment. Each element in design contains:

  - *Name*: name of the variable.
  - *Uncoded*: uncoded levels of the variable, if available in the original dataset.
  - *Coded*: coded levels of the variables.
  - *Levels*: number of levels.
  - *Units*: physical units for the uncoded levels, if available in the original dataset.

- **Response**: the different response variables of the experiment. Each element is a different response variable and contains:

  - *Name*: name of the variable.
  - *Value*: actual values of response variable for each experimental run.
  - *Units*: physical units of the response variable if available.

- **Multilevel**: flag indicating if the experiment has factors with different number of levels.
- **Description**: a more detailed description of the experiment and the variables used.
- **DOI**: a DOI string to identify the source of the data.
- **Source**: another reference to the source of the original dataset, if the DOI is not available.
- **Keywords**: a list of keywords to identify the main characteristics of the experiment.
