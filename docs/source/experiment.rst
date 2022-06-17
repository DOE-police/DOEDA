.. _experiment:

Experiment file
===============

Experiments are stored as YAML files.
All elements in the file are key-value pairs, where the value can sometimes be a list that contains several elements.
In this section we detail each key-value pair present in an experiment file.

Title
-----

A maximum of 15 words to identify and quickly describe the experiment.

Run size
--------

The number of experimental runs in the experiment.

Dataset
-------

Field containing the actual dataset.
Each element of the field represents a factor of the design (or a explanatory variable in the dataset) and contains itself four elements:

Name
^^^^

Name of the factor.
If no name is given, default is :math:`X_{i}` for the :math:`i` th variable.

Uncoded
^^^^^^^

Uncoded levels of the factor.
This is a list where each element represents a single run.
If the uncoded levels are not available, this field is **NA**.

Coded
^^^^^

Coded levels of the factor.
This is a list where each element represents a single run.
If the factor has two levels, they are denoted as -1 and +1.
If the factor has three levels, they are denoted as -1, 0 and +1.
For any other number of levels :math:`n`, the levels are denoted from 0 to :math:`n`.

Units
^^^^^

Units of the factor if it has a name and a physical meaning.
If no units are available, this field is **NA**.

Response
--------

Field containing the response variables of the dataset.
Each element of the field represents a response variable (or a explanatory variable in the dataset) and contains itself three elements:

Name
^^^^

Name of the variable.
If no name is given, default is :math:`X_{i}` for the :math:`i` th variable (starting from the first factor).

Value
^^^^^

Value of the response variable for each run.
This is a list where each element represents a single run.

Units
^^^^^

Units of the response variable if it has a name and a physical meaning.
If no units are available, this field is **NA**.


Multilevel
----------

A TRUE/FALSE value to indicate if the design has factors with different number of levels.

Description
-----------

A detailed description of the experiment.
It should explain the goal of the experiment, the variables studied and measured and if needed some context.
Examples of descriptions can be seen in the :ref:`list of experiments <experiment-list>`.
A description can contain a maximum of 250 words.

DOI
---

The DOI is a unique identifier for a published object available online.
DOI are of the form "https://doi.org/10.1109/5.771073" but the first part of the URL should not be submitted here (i.e. the "https://doi.org" part).
To ensure that a DOI has a recommended format, you can try it `here <https://regexr.com/6nuv3>`.
If it does not pass the test, then it should be referred to as a source and not a DOI.

Source
------

Another way of referring the source of the data if the DOI is not available or if the DOI does not follow the correct format.

Keywords
--------

A list of maximum 3 words to identify the main characteristics of the design.
The list of all available keywords is available in the :ref:`glossary <glossary>`.
