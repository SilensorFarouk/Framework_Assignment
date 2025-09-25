# CORD-19 Analysis Report

## Findings
- **Publications Over Time:** Peaked in 2020 with ~5,000 papers in sample, reflecting COVID surge.
- **Top Journals:** medRxiv and The Lancet dominate, indicating preprint and high-impact focus.
- **Title Words:** Common terms like "COVID-19", "SARS-CoV-2" highlight research themes.
- **Sources:** PMC (40%) is primary, followed by bioRxiv for preprints.

## Challenges
- Missing data: ~30% abstracts empty; handled by filling.
- Large file: Used sampling to speed up.
- Learning: Pandas datetime conversion was tricky; Streamlit caching improved performance.

## What I Learned
- Data workflow: Load → Clean → Analyze → Visualize → Deploy.
- Tools: Streamlit makes interactivity easy; word clouds add visual appeal.

Repo: [Your GitHub URL]