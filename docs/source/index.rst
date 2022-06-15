DOEDA's documentation!
======================

Design of Experiments Database, or DOEDA, is a database that gathers information about experiments that were performed using an experimental design.
The main goal of DOEDA is to provide a central interface to easily access all experiments.

Each experiment in the database is stored as an 'experiment file',
that contains information about the experiment such as the title, a description, the source,
the design and the data.
A full list of all the attributes present in an experiment file is available in the
:ref:`experiment` section.

In order to easily sort the datasets using their characteristics,
each experiment is also given a few keywords to identify its characteristics.
The list of all the keywords and their definition is presented in the :ref:`glossary`
section.

Several tools are also available to turn a datafile into an experiment file, or to recode the levels of factors in a datafile.
All the tools are listed and explained with examples in the :ref:`examples` section.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   experiment.rst
   glossary.rst
   examples.rst
   validation.rst
   experiment_list.rst
