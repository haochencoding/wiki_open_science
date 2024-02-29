# Introduction
This repository hosts the code for the team D1's open science Wikipedia project at Learning Planet Institute. To access the research report, please click this [link](https://docs.google.com/document/d/1HLqHiXIKEWIRQbYrI8TeKe8jfwdV8UT-46aDnhJkzlg/edit?usp=sharing). 

The member of team D1 includes (alphabetical order): Daniela López, Hao Chen, Jawad Anwar, Kristina Chaikina, and Zosia Samsel.

## Installation

Clone the repository:

```bash
git clone https://github.com/haochencoding/wiki_open_science
cd wiki_open_science
```

Create & activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies (inside the virtual environment):

```bash
python -m pip install -r requirements.txt
```

## Directory Tree

Below is the directory tree for the code. Most of the code is located in the `utils` and `notebook` folder.

```
wikipedia_open_science/
│
├── data/
│   ├── abusefilter_logs/        # Abusefilter logs data, scraped from Wikipedia API
│   │
│   ├── abuselogs/               # Edit abuse logs data, scraped from Wikipedia API
│   │
│   ├── block_logs/              # Block policies data, manually indexed from Wikipedia
│   │
│   ├── block_logs/              # Block logs data, scraped from Wikipedia API
│   │
│   ├── merged_data/             # Cleaned and merged data for analysis
│   │
│   ├── scraped_data_metrics/    # Metrics calculated based on scraped data
│   │  
│   └── wikimedia_data/          # User activity metrics from Wikimedia
│  
├── notebooks/  
│   ├── analyze_blocklog_PartA_merge.ipynb  # Code for data merge
│   │
│   ├── analyze_blocklog_PartB_visualization.ipynb  # Code for Data visualisation
│   │
│   ├── calculate_block_log_metrics.ipynb   # Code for metrics calculation for block logs
│   │
│   ├── fetch_block_log_data.ipynb   # Code for block log retrieval from Wikipedia API
│   │
│   └── identify_bots.ipynb     # Code for bot identification
│
└── utils/  
    ├── data_processing.py      # Functions for cleaning and processing raw data
    │
    ├── file_processing.ipynb   # Functions for iterating over raw data csv files
    │
    ├── name_extraction.py      # Functions for extracting names from block log data
    │
    └── spiders.py              # Functions for block log retrieval from Wikipedia API
```