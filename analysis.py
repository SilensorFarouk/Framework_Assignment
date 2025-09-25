import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re
import os  # For file checks

# Set style for better plots
plt.style.use('seaborn-v0_8')  # Note: If this fails, use 'default'
sns.set_palette("husl")

print("Starting CORD-19 Data Analysis...")

# Part 1: Data Loading and Basic Exploration
print("\n=== Part 1: Loading and Exploring Data ===")

# Check if metadata.csv exists
if not os.path.exists('metadata.csv'):
    raise FileNotFoundError("metadata.csv not found! Download it from Kaggle and place in the project root.")

# Load the data (sample 10,000 rows for speed; adjust nrows if needed)
df = pd.read_csv('metadata.csv', nrows=10000)
print("Dataset loaded successfully.")

# Examine first few rows
print("\nFirst 5 rows:")
print(df.head())

# Data structure
print(f"\nDataset dimensions: {df.shape} (rows, columns)")

# Data types
print("\nData types:")
print(df.dtypes)

# Missing values in important columns
important_cols = ['title', 'abstract', 'publish_time', 'journal', 'authors']
print("\nMissing values in important columns:")
print(df[important_cols].isnull().sum())

# Basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df.describe())

# Part 2: Data Cleaning and Preparation
print("\n=== Part 2: Cleaning and Preparing Data ===")

# Handle missing data
df_clean = df.dropna(subset=['title'])  # Drop rows without title
df_clean['abstract'] = df_clean['abstract'].fillna('')  # Fill empty abstracts
df_clean = df_clean.dropna(subset=['publish_time'])  # Drop invalid dates

# Convert to datetime and extract year
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
df_clean['year'] = df_clean['publish_time'].dt.year

# Drop rows where year extraction failed (NaT)
df_clean = df_clean.dropna(subset=['year'])

# Create new column: abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(x.split()) if x else 0)

# Save cleaned data
df_clean.to_csv('cleaned_metadata.csv', index=False)
print(f"Cleaned data saved to 'cleaned_metadata.csv' (shape: {df_clean.shape})")

# Check cleaned data
print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())
print("\nYear distribution:")
print(df_clean['year'].value_counts().sort_index())

# Part 3: Data Analysis and Visualization
print("\n=== Part 3: Analysis and Visualizations ===")

# 1. Papers by publication year
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title('Number of COVID-19 Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.savefig('publications_by_year.png', dpi=300, bbox_inches='tight')
plt.show()
print("Saved: publications_by_year.png")

# 2. Top journals (top 10)
journal_counts = df_clean['journal'].value_counts().head(10)
plt.figure(figsize=(12, 6))
plt.barh(journal_counts.index, journal_counts.values)
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.savefig('top_journals.png', dpi=300, bbox_inches='tight')
plt.show()
print("Saved: top_journals.png")

# 3. Most frequent words in titles (simple)
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation
    return [w for w in text.split() if len(w) > 2]  # Ignore short words

all_titles = ' '.join(df_clean['title'].dropna())
words = clean_text(all_titles)
word_freq = Counter(words)
common_words = word_freq.most_common(20)
print("\nTop 20 words in titles:")
for word, count in common_words:
    print(f"  {word}: {count}")

# Word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.savefig('title_wordcloud.png', dpi=300, bbox_inches='tight')
plt.show()
print("Saved: title_wordcloud.png")

# 4. Distribution by source
source_counts = df_clean['source_x'].value_counts()
plt.figure(figsize=(8, 5))
plt.pie(source_counts.values, labels=source_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Papers by Source')
plt.savefig('papers_by_source.png', dpi=300, bbox_inches='tight')
plt.show()
print("Saved: papers_by_source.png")

print("\n=== Analysis Complete! ===")
print("Generated files: cleaned_metadata.csv, publications_by_year.png, top_journals.png, title_wordcloud.png, papers_by_source.png")
print("Now run: streamlit run streamlit_app.py")
