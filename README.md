
# CORD-19 Data Analysis and Streamlit Explorer

![COVID-19 Research](https://img.shields.io/badge/Project-CORD--19-blue?style=flat-square) ![Python](https://img.shields.io/badge/Python-3.7%2B-yellow?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-App-orange?style=flat-square)

## Overview

This repo analyzes the CORD-19 dataset's `metadata.csv` for COVID-19 research papers. It includes data cleaning, exploratory analysis, visualizations (e.g., publication trends, top journals, word clouds), and an interactive Streamlit app. Built for the Frameworks_Assignment, showcasing pandas, matplotlib/seaborn, and Streamlit skills. Dataset: [Kaggle CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

## Installation

1. **Clone Repo:**
   ```
   git clone https://github.com/SilensorFarouk/Frameworks_Assignment.git
   cd Frameworks_Assignment
   ```

2. **Download Dataset:**
   - Get `metadata.csv` from Kaggle and place in root (samples ~10k rows for speed).

3. **Install Packages:**
   ```
   pip install pandas matplotlib seaborn streamlit wordcloud numpy
   ```

## Usage

### 1. Run Analysis (Required First)
```
python analysis.py
```
- Loads/cleans data, prints stats (e.g., shape, missing values, top words).
- Saves `cleaned_metadata.csv` and PNG plots (e.g., `publications_by_year.png`).
- Runtime: ~30-60s. Plots pop up—close after viewing.

### 2. Run Streamlit App
```
streamlit run streamlit_app.py
```
- Opens in browser (localhost:8501).
- Features: Sidebar filters (years, top journals), dynamic plots, data table, quick stats.
- Ignore "ScriptRunContext" warnings.

## File Structure

```
Frameworks_Assignment/
├── README.md                 # This file
├── metadata.csv              # Raw dataset (download here)
├── analysis.py               # Cleaning, analysis, plots
├── streamlit_app.py          # Interactive app
├── cleaned_metadata.csv      # Generated cleaned data
├── *.png                     # Generated plots (year, journals, wordcloud, sources)
└── report.md              # Findings reflection
```

## Key Findings

- **Trends:** Publications peaked in 2020 (~60-70% of sample).
- **Journals:** Led by medRxiv, bioRxiv, The Lancet.
- **Titles:** Common words: "COVID-19", "SARS-CoV-2", "coronavirus".
- **Sources:** PMC (~40%), bioRxiv (~30%).
- Sample: ~8,500 cleaned rows; ~30% abstracts missing.

## Challenges and Reflection

- **Challenges:** Missing dates (handled via `pd.to_datetime`), large file (sampled), OneDrive sync issues.
- **Learnings:** Pandas for cleaning; Streamlit for easy interactivity. Workflow: Load → Clean → Visualize → Deploy.
- **Time:** ~10 hours; great intro to data science.

## Submission

For Frameworks_Assignment: https://github.com/SilensorFarouk/Frameworks_Assignment.

Contact: silensorfarouk@gmail.com. 


---

*Updated: 25th September 2025*
```
