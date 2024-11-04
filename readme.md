# Code Completion Evaluation Project

This repository contains the implementation and evaluation of code completion using the tiny_starcoder model. The project focuses on the fill-in-the-middle approach, where code segments are split into three parts (prefix, middle, and suffix), and the model attempts to predict the middle part.

## Project Structure
```
├── dataset/
│   ├── dataset.txt                # Human-readable dataset with all information
│   └── json/
│       ├── dataset.json           # Initial dataset with code splits and predictions
│       ├── dataset_reviewed.json  # Dataset with manual reviews and comments
│       ├── dataset_final.json     # Final dataset with reviews and metrics
│       └── raw_outputs.json       # Raw outputs from tiny_starcoder model
│
├── review.md                      # Project report and findings
└── src/
    ├── code_split_script.py       # Script for splitting code into three parts
    ├── metrics.ipynb              # Jupyter notebook with metric calculations and visualizations
    ├── review.py                  # Script for manual review process
    └── tiny_starcoder.py          # Code for running tiny_starcoder model
```

## Implementation Details
- **Code Splitting**: Implemented in `code_split_script.py`, splits source code into prefix, middle, and suffix parts
- **Model**: Uses tiny_starcoder for code completion predictions
- **Evaluation**: Combines manual review (1-5 scale) with automatic metrics (Exact Match, CHRF, BLEU, ROUGE-L, Levenshtein)
- **Visualization**: Includes correlation analysis and metric comparisons in `metrics.ipynb`

## Results
The complete analysis and findings can be found in `review.md`. Key findings include:
