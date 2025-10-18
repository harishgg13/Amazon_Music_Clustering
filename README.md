# 🎵 Amazon Music Clustering & Genre Prediction App

## 🧩 Project Title  
**Amazon Music Clustering**

---

## 🎯 Problem Statement
With millions of songs available on platforms like Amazon Music, manually categorizing tracks into genres or moods is impractical.  
This project aims to **automatically group songs** based on their **audio characteristics** using **unsupervised machine learning (clustering)**.  

By analyzing features like **tempo**, **energy**, **danceability**, and **acousticness**, the project identifies **natural clusters** that represent **musical genres or moods** — without requiring prior labels.

---

## 💼 Business Use Cases
- 🎧 **Personalized Playlist Curation:** Automatically group songs that sound similar to enhance playlist generation.  
- 🔍 **Improved Song Discovery:** Suggest similar tracks based on audio profiles.  
- 🎤 **Artist Analysis:** Identify competitor songs within similar sound clusters.  
- 📊 **Market Segmentation:** Enable streaming platforms to analyze user listening trends and optimize recommendations.

---

## 🧠 Skills Takeaway
`Data exploration` • `Data cleaning` • `Feature selection` • `Data normalization`  
`K-Means clustering` • `Elbow method` • `Silhouette score` • `PCA` • `Cluster visualization`  
`Genre inference` • `Python (Pandas, NumPy, scikit-learn)` • `Data storytelling`

---

## 🌍 Domain  
**Music Analytics / Unsupervised Machine Learning**

---

## 🧪 Approach Overview

### 1️⃣ Data Exploration & Preprocessing
- Loaded and explored the dataset `single_genre_artists.csv`
- Handled missing values and duplicates  
- Dropped non-numerical columns: `track_name`, `artist_name`, `track_id`
- Scaled numeric features using **StandardScaler**

### 2️⃣ Feature Selection
**Selected features:**
```
['danceability', 'energy', 'loudness', 'speechiness',
 'acousticness', 'instrumentalness', 'liveness',
 'valence', 'tempo', 'duration_ms']
```
These features represent rhythm, mood, and instrumentation of songs.

### 3️⃣ Dimensionality Reduction
Applied **PCA (Principal Component Analysis)** to reduce data dimensions and visualize clusters in 2D space.

### 4️⃣ Clustering Techniques
**Main Algorithm:** K-Means  
- Determined optimal *k* using:
  - Elbow Method (Inertia)
  - Silhouette Score  
- Also tested **DBSCAN** 

### 5️⃣ Cluster Evaluation
| Metric | Description |
|---------|--------------|
| **Silhouette Score** | Measures how well each song fits its cluster |
| **Davies–Bouldin Index** | Lower = better separation |
| **Inertia (KMeans)** | Measures compactness of clusters |

---

## 📊 Results & Interpretation

Three distinct clusters emerged:

| Cluster | Genre | Characteristics |
|----------|--------|-----------------|
| **0** | **Pop / Dance / Electronic** | High energy, loud, rhythmic, less acoustic |
| **1** | **Acoustic / Ballad / Indie** | Soft, high acousticness, low loudness, calm |
| **2** | **Rap / Hip-Hop / Spoken Word** | High speechiness, live feel, less melodic |

---

## 🧩 Streamlit Application

### 🎶 Song Genre Prediction
Predict a song’s genre by:
- Entering song features manually  
- Or selecting an existing song  

### 🎧 Mood-Based Song Recommendation
Pick your mood (e.g., *Happy, Sad, Party, Focus*) → app recommends songs that fit that vibe.

### 💿 Genre-Based Song Recommendation
Select a genre and get 30 sample songs from that category.

---

## 🧱 Tech Stack

| Category | Tools |
|-----------|-------|
| **Language** | Python |
| **ML/Analytics** | Pandas, NumPy, scikit-learn |
| **Modeling** | K-Means, PCA |
| **Frontend** | Streamlit |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Streamlit Cloud / Local |

---

## 🗂️ Project Structure

```
📁 Amazon_Music_Clustering/
│
├── app.py                     # Main Streamlit app (genre prediction)
├── Similar_song.py             # Mood/genre-based recommendation module
├── PP.ipynb                    # Preprocessing & model training notebook
├── model.pkl                   # Trained K-Means model
├── scalar.pkl                  # StandardScaler object
├── pca_data_fit.pkl            # PCA transformation object
├── pca_data_transform.pkl      # PCA-transformed dataset
├── prediction_in_original.csv  # Final dataset with predictions
└── README.md                   # Project documentation
```

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/harishgg13/Amazon_Music_Clustering.git
cd Amazon-Music-Clustering

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 🧠 Model Summary

- **Algorithm:** KMeans (k=3)
- **Scaler:** StandardScaler
- **Dimensionality Reduction:** PCA (2 Components)
- **Evaluation Metrics:** Silhouette Score, Davies–Bouldin Index
- **Genre Mapping:**
  ```python
  {0: "Pop / Dance / Electronic",
   1: "Acoustic / Ballad / Indie",
   2: "Rap / Hip-Hop / Spoken Word"}
  ```

---

## 🧾 Deliverables
- ✅ Preprocessing, clustering, and visualization scripts (`.ipynb` or `.py`)
- ✅ Final dataset (`prediction_in_original.csv`)
- ✅ Streamlit App for interactive predictions
- ✅ Final report summarizing clusters and interpretations

---

## 📅 Timeline
The project must be completed and submitted within **10 days** from assignment.

---

## 🧭 References
- EDA & Capstone Guidelines (GUVI)
- GitHub Reference Guide
- Clustering Algorithms (scikit-learn Documentation)

---

## 👨‍💻 Author
**G G Harish**  
Data Science Enthusiast | Streamlit Developer  
📧 [harishgg03@gmail.com](mailto:harishgg03@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/ggharish13) | [GitHub](https://github.com/harishgg13)
