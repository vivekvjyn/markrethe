Overview
============

Markrethe is a Python package for writing Markdown logs for research experiments.
It provides a simple API to generate well-formatted Markdown files programmatically.

Installation
------------

Install from GitHub:

.. code-block:: bash

    pip install git+https://github.com/vivekvjyn/markrethe.git

Quick Start
-----------

.. code-block:: python

    from markrethe import Markrethe

    m = Markrethe("./logs")
    m.heading("Experiment 1")
    m.paragraph("Starting the experiment...")
    m.bold("Key finding:")
    m.table(["Metric", "Value"], [["Accuracy", "95%"]])
