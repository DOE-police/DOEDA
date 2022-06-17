.. _examples:

Examples
========

**Ceramic experiment**: converting csv data files to yaml experiment files
--------------------------------------------------------------------------

In this section, we present an example of how to use the ``csv2json.py``
script, stored in the ``utils\`` fodler, to generate the experiment file from a csv file.

In this example, we look at an experiment published by Bouler et
al. (1996) that was used as an example in the book of Mee (2000). In
this experiment, researchers studied the compressive strength of MBCP
samples based on five parameters used during the creation of the
samples. To perform the experiment, they used a fractional factorial
design with additional center runs. The data of the experiment is stored
in the csv file called ``ceramic_experiment.csv``, which contains the
following columns:

-  The 5 explanatory variables with 3 levels, in coded form (-1,0,1), in
   columns 1 to 5
-  The response variable in the last column

To better visualize the format of the file, a subset of the rows is
presented in the table below.

+---------------+---------------------------+-----------------------------+----------------------------+----------------------------+----------------+
| HA in BCP (%) | Weight of naphthalene (%) | Diameter of macropores (µm) | Isostatic compaction (kPa) | Sintering temperature (°C) | Strength (mPa) |
+===============+===========================+=============================+============================+============================+================+
| -1            | -1                        | -1                          | -1                         | -1                         | 2.2            |
+---------------+---------------------------+-----------------------------+----------------------------+----------------------------+----------------+
| 1             | -1                        | -1                          | -1                         | 1                          | 7.0            |
+---------------+---------------------------+-----------------------------+----------------------------+----------------------------+----------------+
| 0             | 0                         | 0                           | 0                          | 0                          | 10.8           |
+---------------+---------------------------+-----------------------------+----------------------------+----------------------------+----------------+
| 0             | 0                         | 0                           | 0                          | 0                          | 11.5           |
+---------------+---------------------------+-----------------------------+----------------------------+----------------------------+----------------+
| -1            | -1                        | 1                           | 1                          | -1                         | 11.7           |
+---------------+---------------------------+-----------------------------+----------------------------+----------------------------+----------------+
| 1             | -1                        | 1                           | 1                          | -1                         | 12.3           |
+---------------+---------------------------+-----------------------------+----------------------------+----------------------------+----------------+

We use the ``--header`` option to specify that the variables names are
given in the first row of the file.

Since the units are given between brackets at the end of each variable
name, we specify that by using the ``--units`` option.

The levels of the factors are not the real levels used by practitioners
during the experiment, they have been recoded to standard levels (-1, 0
and 1 in this case), so we use the ``--coded`` option.

The last column of the file gives the response values, obtained once the
experiment was completed. Since there is only one response variable, we
specify it by using the ``--response 1`` option.

We want to name our experiment “Ceramic strength experiment” so we
specify with the ``--title "Ceramic strength experiment`` option.

As mentionned earlier, the data is taken from the 1996 paper of Boulers et al., available on `this <https://doi.org/10.1002/(SICI)1097-4636(199612)32:4<603::AID-JBM13>3.0.CO;2-E>` webiste.
It can be identified by its unique DOI.
To add it to the experiment file, we use the
``--doi "https://doi.org/10.1002/(SICI)1097-4636(199612)32:4<603::AID-JBM13>3.0.CO;2-E"``
option.

Finally, we provide a small description of the experiment.
The abstract of the paper is:

    Compressive strength measurements were conducted on 32 macroporous biphasic calcium phosphate (MBCP) samples to evaluate the influences and interactions of five synthesis factors: chemical composition, percentage of macropores, mean size of macropores, isostatic compaction pressure, and sintering temperature.
    These parameters were varied simultaneously between two limit levels.
    Experiments used a factorial design method (FDM) allowing optimization of the number of samples as well as statistical analysis of results.
    FDM showed that compressive strength, in a defined experimental area, can be described by a first-order polynomial equation in which the percentage of macroporosity and sintering temperature are the major influences.
    This study leads up to an isoresponse line diagram that will allow the manufacture of some classes of MBCP with fitted compressive strength.

The first sentence is a good short description of the experiment.
We add it to the experimental file by using the following option:

.. code:: bash

   --description "Compressive strength measurements were conducted on 32 macroporous biphasic calcium phosphate (MBCP) samples to evaluate the influences and interactions of five synthesis factors: chemical composition, percentage of macropores, mean size of macropores, isostatic compaction pressure, and sintering temperature"

Finally, we said that the design used in the experiment was a fractional
factorial design with additional center runs. To specify these
attributes in the experiment file, we use keywords with the following
options: ``-k cener-runs`` and ``-k fractional-factorial``.

All these statements are actually optional and will either be infered
from the dataset or set to ``null`` if a value is not specified when
using the script. However, two arguments are required when using the
script:

-  the path of the csv file containing the data set
-  the path of the yaml experiment file that will be created

When we combine all these together, we obtain the following command:

.. code:: bash

   python csv2json.py --header --units --coded --response 1 --title "Ceramic strength experiment" --doi "https://doi.org/10.1002/(SICI)1097-4636(199612)32:4<603::AID-JBM13>3.0.CO;2-E" --description "Compressive strength measurements were conducted on 32 macroporous biphasic calcium phosphate (MBCP) samples to evaluate the influences and interactions of five synthesis factors: chemical composition, percentage of macropores, mean size of macropores, isostatic compaction pressure, and sintering temperature" -k center-runs -k fractional-factorial ../csv/ceramic_experiment.csv ../yml/ceramic_experiment.yml


.. TODO: add a section about the recodecsv.py file
