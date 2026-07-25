# Markrethe

A Python package for writing Markdown logs for research experiments.

## Installation

```bash
pip install git+https://github.com/vivekvjyn/markrethe.git
```

## Quick Start

```python
from markrethe import Markrethe

m = Markrethe("./logs")
m.heading("Experiment 1")
m.paragraph("Starting the experiment...")
m.bold("Key finding:")
m.table(["Metric", "Value"], [["Accuracy", "95%"]])
```
