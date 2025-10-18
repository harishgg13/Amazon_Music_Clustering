import seaborn as sns
import pandas as pd
import streamlit as st
import joblib
import matplotlib.pyplot as plt

st.markdown(
    """
    <h1 style='text-align: center; color: white;'>
        Visualizing Clusters
    </h1>
    """,
    unsafe_allow_html=True
)

data=pd.read_csv("prediction_in_original.csv")
data2=pd.read_csv("Data_predicted.csv")
average_data=data2.groupby("cluster").mean()


fig, ax = plt.subplots(figsize=(10, 6))
average_data.plot(kind='bar', ax=ax)

ax.set_title("Average Feature Values per Cluster")
ax.set_xlabel("Cluster")
ax.set_ylabel("Mean Value")
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig)

# ------------------------------------------------------------------------------------------------------------------------------

fig=plt.figure(figsize=(10,6))
sns.heatmap(average_data, annot=True, cmap='coolwarm')
plt.title("Feature Comparison Across Clusters")
plt.show()
st.pyplot(fig)

# ------------------------------------------------------------------------------------------------------------------------------

features = ['danceability', 'energy', 'valence', 'tempo', 
            'acousticness', 'speechiness', 'loudness', 
            'instrumentalness', 'liveness']

fig1=plt.figure(figsize=(10, 6))

for i, feature in enumerate(features, 1):
    plt.subplot(3, 3, i)
    sns.kdeplot(data=data, x=feature, hue='cluster', fill=True, alpha=0.5)
    plt.title(f"{feature} by Cluster", fontsize=10)
    plt.xlabel("")
    plt.ylabel("")
    plt.tight_layout()

plt.suptitle("Feature Distributions by Cluster (3x3 Grid)", fontsize=16, y=1.02)
plt.show()
st.pyplot(fig1)

# ------------------------------------------------------------------------------------------------------------------------------
kmeans_cluster=joblib.load("kmeans_cluster.pkl")
pca_data_transform=joblib.load("pca_data_transform.pkl")

fig, ax = plt.subplots()
ax.scatter(pca_data_transform[:,0], pca_data_transform[:,1], 
           c=kmeans_cluster, cmap='viridis', s=5, alpha=0.6)

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('K-Means Clustering')

st.pyplot(fig)

# ------------------------------------------------------------------------------------------------------------------------------

import streamlit as st
st.markdown("""<h1 style='text-align:center;'> Cluster Interpretation </h1>""",unsafe_allow_html=True)
st.markdown(""" <h4>🎵 Cluster 0 – Pop / Dance / Electronic</h4>

<b> Key features:</b>

<b>High:</b> Energy, Loudness, Danceability, Tempo

<b>Low:</b> Acousticness, Speechiness

<b>Interpretation:</b>
This cluster represents energetic, upbeat, and rhythmic tracks typical of Pop, Dance, or Electronic music.
Songs are loud and dynamic with strong beats, minimal acoustic elements, and low spoken content.

<h4>🎸 Cluster 1 – Acoustic / Ballad / Indie</h4>

<b> Key features: </b>

<b>High:</b> Acousticness, Instrumentalness

<b>Low:</b> Energy, Loudness, Danceability

<b>Interpretation:</b>
This cluster represents soft, melodic, and acoustic-style music such as Ballads or Indie songs.
These tracks have gentle energy, quieter loudness, and rely more on acoustic or instrumental sounds.

<h4>🎤 Cluster 2 – Rap / Hip-Hop / Spoken Word</h4>

<b>Key features:</b>

<b>High:</b> Speechiness, Liveness

<b>Low:</b> Duration, Loudness, Acousticness

<b>Interpretation:</b>
This cluster contains lyric-heavy and performance-oriented tracks typical of Rap, Hip-Hop, or Spoken Word genres.
They have more spoken elements, live or crowd-like energy, and are less focused on melody or loudness.""",unsafe_allow_html=True)