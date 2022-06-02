#!/bin/bash
python utils/data_processing/csv2json.py csv/polyethylene_film_recoded.csv experiments/polyethylene_film.yaml \
--header \
--units \
--uncoded \
--response 4 \
--title "Polyethylene film" \
--description 'The simultaneous effects of a range of additives and associated interactions on meltprocessing stability, processing discoloration, and long-term stability of a blown film-grade metallocene LLDPE (mLLDPE) were investigated by using a two-level factorialexperimental design. The experiment was ran in blocks, where each block is a separate day, and the nine runs within each block were performed sequentially. The responses are two stability measures (melt flow rate after the first and third extruder passes;S1 and S3, respectively), a yellowness index after the third pass (YI), and a measure of long-term oxidation at 100°C (T); specifically, T is the number of hours until a carbonyl index reaches a specified level. This example was taken from chapter 2 of the book "A Comprehensive Guide to Factorial Two-level Experimentation" (2009) by Robert Mee.' \
--doi "10.1002/vnl.20022" \
-k center-runs \
-k blocking \
-k full-factorial \
--sep ";" \
--decimal ","