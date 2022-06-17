.. _glossary:

Glossary
========

Glossary of all experiment attributes with short definitions.

.. glossary::
  :sorted:

  Blocking
    Blocking an experiment means that the runs are grouped according to one or more factors, usually not controlled by the experimenters, such that all the runs are not randomized.
    The experiment is then separated in blocks, defined by the blocking factors.

  Center runs
    Exprimental runs where all factors are set at the intermediate level (coded as 0).
    They are usually added in a design to provide an unbiased estimate of the variance or to perform lack-of-fit tests.
    Know aliases: center points, controls runs.

  Fractional factorial
    A design that is the fraction of a full-factorial design.
    A full-factorial :math:`2^{k}` contains all combinations of the levels of :math:`k` factors.

  Full factorial
    A full-factorial :math:`2^{k}` contains all combinations of the levels of :math:`k` factors.

  RCBD
    Randomized Complete Block Design, or RCBD, is a blocked design
    (see :term:`blocking <Blocking>` ), where each treatment appears exactly once in each block.
    It is commonly used in argicultural field trials.

  DSD
    To be done

  Foldover
    To be done

  Screening
    To be done

  Plackett-Burman
    Plackett-Burman (PB) designs are :term:`saturated <Saturated>` designs for two-level factors where the run size is a multiple of four.
    However, when the run size is also a power of two, the design is equivalent to a :term:`Fractional factorial<fractional factorial>` design.
    Therefore, it is mainly used when the run size is a multiple of four, but not a power of two.
    In PB designs, for any two factors, all combinations of levels appear the same number of times.

  Saturated
    A design is said to be saturated when there are :math:`k` factors and :math:`k+1` runs.
