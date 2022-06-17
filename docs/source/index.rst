DOEDA's documentation
======================

Design of Experiments Database, or DOEDA, is a database that contains information and data sets about experiments that were performed using an experimental design.
The main goal of DOEDA is to provide a central interface to easily access all experiments.

Each experiment in the database is stored as an :ref:`experiment file <experiment>`, that contains both the actual data set and some information about the experiment such as the title, a description, the source.
The experiments are also given a few keywords to identify their characteristics.
The list of all the keywords and their definition is presented in the :ref:`glossary <glossary>`.
A list of all the experiment of the database (with their name, description and keywords) is presented in :ref:`this section <experiment-list>`.

Since many datasets are often available as csv or text file, we created a tool to create an experiment file from a csv file.
Several other tools are also available and explained with :ref:`examples <examples>`.

.. TODO: refactor validation and schemes + add description in the intro

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   experiment.rst
   glossary.rst
   examples.rst
   validation.rst
   experiment_list.rst
