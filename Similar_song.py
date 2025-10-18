import joblib
import pandas as pd
import streamlit as st
import numpy as np
import random

st.markdown(
    """
    <h1 style='text-align: center; color: white;'>
        What’s Your Mood Today?
    </h1>
    """,
    unsafe_allow_html=True
)

def cal(Pca_transform,target):
    df=pd.DataFrame({"x": Pca_transform[:, 0].tolist(),
        "y": Pca_transform[:, 1].tolist()})
    df['distance'] = np.sqrt((df['x'] - target[0][0])**2 + (df['y'] - target[0][1])**2)
    nearest_points = df.nsmallest(30, 'distance')

    Song_df=pd.read_csv("prediction_in_original.csv")
    # similarSong=Song_df.iloc[nearest_points.index]
    st.write(f"Based on your selected mood, here are the top songs you’ll love :")
    col1,col2,col3=st.columns([1,1,1])

    with col1:
        for a,b in zip(nearest_points.index[0:10],range(1,len(nearest_points.index)+1)):
            st.write(f"{b}. {Song_df.iloc[a]["name_song"]} by {Song_df.iloc[a]["name_artists"]}")
    with col2:
        for a,b in zip(nearest_points.index[10:20],range(11,21)):
            st.write(f"{b}. {Song_df.iloc[a]["name_song"]} by {Song_df.iloc[a]["name_artists"]}")
    with col3:
        for a,b in zip(nearest_points.index[20:30],range(21,31)):
            st.write(f"{b}. {Song_df.iloc[a]["name_song"]} by {Song_df.iloc[a]["name_artists"]}")

# ------------------------------------------------------------------------------------------------------------------------------

options=st.radio("",["Song by mood","Song by Genre"],horizontal=True)

if options == "Song by mood":
    moods = [
        "Happy", "Energetic", "Motivated", "Confident",
        "Chill", "Romantic", "Nostalgic", "Sad", "Peaceful",
        "Dramatic", "Mysterious", "Powerful",
        "Party", "Dance", "Travel", "Workout", "Focus", "Late Night", "Rainy Day"
    ]
    mood = st.selectbox("Select your mood or vibe 🎭", moods)

    mood_features = {
        "Happy": [210000, 0.75, 0.80, -6, 0.05, 0.10, 0.00, 0.15, 0.90, 120.0],
        "Energetic": [200000, 0.80, 0.90, -4, 0.04, 0.05, 0.00, 0.20, 0.85, 130.0],
        "Motivated": [220000, 0.70, 0.85, -5, 0.03, 0.10, 0.00, 0.18, 0.88, 125.0],
        "Confident": [210000, 0.68, 0.88, -5, 0.04, 0.08, 0.00, 0.15, 0.85, 128.0],
        "Chill": [240000, 0.55, 0.40, -12, 0.04, 0.50, 0.05, 0.12, 0.70, 90.0],
        "Romantic": [230000, 0.60, 0.50, -10, 0.05, 0.40, 0.02, 0.10, 0.75, 95.0],
        "Nostalgic": [250000, 0.50, 0.45, -11, 0.05, 0.55, 0.10, 0.12, 0.65, 88.0],
        "Sad": [260000, 0.40, 0.30, -15, 0.06, 0.60, 0.15, 0.10, 0.35, 80.0],
        "Peaceful": [240000, 0.45, 0.35, -14, 0.03, 0.70, 0.20, 0.10, 0.60, 85.0],
        "Dramatic": [220000, 0.60, 0.70, -8, 0.05, 0.25, 0.05, 0.18, 0.50, 110.0],
        "Mysterious": [230000, 0.50, 0.60, -10, 0.06, 0.35, 0.10, 0.15, 0.45, 105.0],
        "Powerful": [210000, 0.70, 0.92, -4, 0.03, 0.05, 0.00, 0.20, 0.88, 132.0],
        "Party": [200000, 0.85, 0.90, -3, 0.04, 0.05, 0.00, 0.25, 0.92, 128.0],
        "Dance": [195000, 0.88, 0.88, -5, 0.04, 0.05, 0.00, 0.20, 0.90, 130.0],
        "Travel": [230000, 0.65, 0.70, -8, 0.04, 0.20, 0.05, 0.18, 0.75, 120.0],
        "Workout": [210000, 0.80, 0.92, -4, 0.03, 0.05, 0.00, 0.20, 0.85, 130.0],
        "Focus": [250000, 0.30, 0.25, -16, 0.05, 0.70, 0.60, 0.10, 0.40, 75.0],
        "Late Night": [240000, 0.50, 0.55, -12, 0.05, 0.50, 0.20, 0.15, 0.60, 90.0],
        "Rainy Day": [260000, 0.40, 0.35, -15, 0.05, 0.60, 0.25, 0.12, 0.50, 80.0]
    }

    features = mood_features[mood]
    features_array = np.array(features).reshape(1, -1)
    scalar=joblib.load("scalar.pkl")
    scaled_input=scalar.transform(features_array)

    pca_fit=joblib.load("pca_data_fit.pkl")
    Pca_transform_data=joblib.load("pca_data_transform.pkl")
    pca=pca_fit.transform(scaled_input)

    target_data=pca.tolist()
    pred=cal(Pca_transform_data,target_data)

# ------------------------------------------------------------------------------------------------------------------------------

if options == "Song by Genre":

    Genre_option=st.selectbox("Choose the Genre",["1. Pop / Dance / Electronic","2. Acoustic / Ballad / Indie","3. Rap / Hip-Hop / Spoken-word"])
    df=pd.read_csv("prediction_in_original.csv")
    rand_int = random.randint(1, 100)
    sample=df.sample(n=30,random_state=rand_int)
    index_list=list(sample.index)
    col1,col2,col3=st.columns([1,1,1])

    with col1:
        for a in range(0,10):
            st.write(f"{a+1}. {sample.iloc[a]["name_song"]} by {sample.iloc[a]["name_artists"]}")
    with col2:
        for a in range(10,20):
            st.write(f"{a+1}. {sample.iloc[a]["name_song"]} by {sample.iloc[a]["name_artists"]}")
    with col3:
        for a in range(20,30):
            st.write(f"{a+1}. {sample.iloc[a]["name_song"]} by {sample.iloc[a]["name_artists"]}")
