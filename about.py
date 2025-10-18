import streamlit as st

st.title("About This Project")

st.markdown("""
**Amazon Music Clustering** is an interactive web application designed to analyze and visualize the vast collection of songs on Amazon Music. 
By leveraging machine learning techniques, this app groups songs into clusters based on their audio features, enabling users to discover patterns, trends, and similarities in music effortlessly.

The application is ideal for music enthusiasts, researchers, or developers interested in exploring audio data and understanding musical trends through data-driven insights.

**Key Features:**
- **Clustering Analysis:** Uses K-Means clustering to group songs based on features such as tempo, energy, danceability, acousticness, and more.
- **Interactive Visualizations:** Scatter plots, bar charts, and heatmaps help visualize clusters and feature distributions.
- **Nearest Song Recommendations:** Find songs similar to a selected track within the same cluster.
- **Feature Exploration:** Understand which attributes contribute most to a song’s placement within a cluster.

**Technology Stack:**
- **Frontend & Deployment:** Streamlit for building an interactive web interface.
- **Data Processing & Machine Learning:** Python, Pandas, NumPy, Scikit-learn.
- **Visualization:** Matplotlib, Seaborn, Plotly for interactive charts.
- **Data Storage:** CSV / DataFrames for song metadata and feature storage.

**How It Works:**
1. The dataset containing song features is preprocessed and scaled.
2. K-Means clustering is applied to identify groups of similar songs.
3. Users can visualize clusters and analyze features interactively.
4. The app provides recommendations based on nearest neighbors within clusters.

This project demonstrates how machine learning and data visualization can simplify music analysis, uncover hidden patterns, and enhance music discovery.
""")
