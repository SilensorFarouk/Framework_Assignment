import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter

# Load cleaned data (assume you've saved it)
@st.cache_data
def load_data():
    return pd.read_csv('cleaned_metadata.csv')

df = load_data()

# Custom function for word freq (reuse from analysis)
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text.split()

# App layout
st.title("🦠 CORD-19 Data Explorer")
st.write("A simple interactive exploration of COVID-19 research papers from the CORD-19 dataset. "
         "Analyze trends in publications, journals, and titles.")

# Sidebar for interactions
st.sidebar.header("Filters")
year_min, year_max = st.sidebar.slider("Select Year Range", 2019, 2022, (2019, 2022))
top_n_journals = st.sidebar.slider("Top N Journals", 5, 15, 10)

# Filter data
filtered_df = df[(df['year'] >= year_min) & (df['year'] <= year_max)]

# Display sample data
st.header("Sample Papers")
if st.checkbox("Show table"):
    st.dataframe(filtered_df[['title', 'authors', 'journal', 'year', 'source_x']].head(10))

# Visualization 1: Publications over time
st.header("Publications by Year")
fig1, ax1 = plt.subplots(figsize=(10, 5))
year_counts = filtered_df['year'].value_counts().sort_index()
ax1.bar(year_counts.index, year_counts.values)
ax1.set_title('Publications by Year (Filtered)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Papers')
st.pyplot(fig1)

# Visualization 2: Top Journals
st.header("Top Publishing Journals")
journal_counts = filtered_df['journal'].value_counts().head(top_n_journals)
fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.barh(journal_counts.index, journal_counts.values)
ax2.set_title(f'Top {top_n_journals} Journals')
ax2.set_xlabel('Number of Papers')
st.pyplot(fig2)

# Visualization 3: Word Cloud (dynamic based on filter)
st.header("Word Cloud of Titles")
all_titles = ' '.join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
ax3.set_title('Word Cloud of Filtered Paper Titles')
st.pyplot(fig3)

# Visualization 4: Sources (pie chart)
st.header("Papers by Source")
source_counts = filtered_df['source_x'].value_counts()
fig4, ax4 = plt.subplots(figsize=(8, 5))
ax4.pie(source_counts.values, labels=source_counts.index, autopct='%1.1f%%')
ax4.set_title('Distribution by Source (Filtered)')
st.pyplot(fig4)

# Stats sidebar
st.sidebar.header("Quick Stats")
st.sidebar.write(f"Total papers (filtered): {len(filtered_df)}")
st.sidebar.write(f"Avg abstract words: {filtered_df['abstract_word_count'].mean():.0f}")