.. _validation:

Schemes
=======

In this section we present the schemes and formats that the different files of this project must have.

CSV files
---------

Comma-separated value (CSV) files can be used with the ``csv2json.py`` script in order to create an experiment file from a data file.
However, to create a correct experiment file, the data file must follow some formatting rules:

* One row corresponds to one experimental run
* One column correspond to one factor
* In term of columns ordering, the columns representing the factors must come before the columns representing the response variable(s)
* The first row of the data must contain the variable names, with the unit of the variable in parenthesis at the end (e.g. "Applied pressure (Pa)")
* The columns must be separated by semi-colon
* For numerical values with decimal numbers, use a comma ',' as the decimal separator

Only the first three formatting rules are mandatory.
The other ones are simply the default options but can be changed when using ``csv2json.py``.

Experiment files
----------------

Experiment files are ``.yaml`` files that follow a specific structure.



Validation
==========

We can use the same script we use in github actions to locally validate experiment files. This script can be found
in ``utils/validation/scripts/validation.py`` in this repository.

Calling

.. code-block:: bash

    python utils/validation/scripts/validation.py --file experiments/test.yaml


we will be validating as experiment the contents of ``test.yaml``.

Calling the script without --file will validate all the yaml files contained in ``experiments/`` folder that were
changed in the current working tree and the main branch tree. We use this functionality in the github action
validation pipeline.

Validation schema
-----------------

show here the schema against which we validate our experiment
Work in progress...

Keywords validation
-------------------

To validate that all the keywords present in the experiment file are described in the glossary, we can use another validation script.
This script can be found
in ``utils/validation/scripts/keywords_validation.py`` in this repository.

Calling

.. code-block:: bash

    python utils/validation/scripts/keywords_validation.py

will simply notify you if any of the keywords are unexplained.
