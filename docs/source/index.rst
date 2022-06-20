DOEDA: an experiment database
=============================

What's DOEDA?
-------------

Design of Experiments Database, or **DOEDA** in short , is a database that contains information and data sets about experiments that were performed using an experimental design.

The main goal of DOEDA is to provide a central interface to easily access all experiments.

Features
--------

Each experiment in DOEDA is stored as an :ref:`experiment file <experiment>`, that contains both the actual data set and some information about the experiment such as the title, a description, the source.
Each experiment is also given a few keywords to identify its main characteristics.
A list of all the keywords and their definition is presented in the :ref:`glossary <glossary>`.
A list of all the experiment contained in the database is presented in the :ref:`list of experiments <experiment-list>`.


Submitting new experiments
--------------------------

If you would like to add an experiment to the database there are two ways of doing so:

#. Using the raw dataset from a ``txt`` or ``csv`` file:
    Since many datasets are often available as csv or text file, we created a tool to create an experiment file from a csv file.
    Usage is explained :ref:`here<examples>` and a detailed documentation is available :ref:`here<tools>`.

#. Directly using an experiment file:
    In order to directly submit an experiment file it must pass the validation checks.
    The required format of the experiment file is explained :ref:`here<validation>`.

Several other tools are also available and explained with :ref:`examples <examples>`.

Contributing
------------

If you have a suggestion that would make this better, please fork the repo and create a pull request.
You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

.. TODO: refactor validation and schemes + add description in the intro

.. toctree::
  :hidden:
  :maxdepth: 2

  experiment
  glossary
  experiment_list
  tools
  examples
  validation
