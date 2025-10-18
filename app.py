import joblib
import numpy as np
import streamlit as st
import pandas as pd
from HTML_CSS import page1_home,page1_footer

if "page" not in st.session_state:
    st.session_state.page = "Song Prediction"

page1_home()

# ------------------------------------------------------------------------------------------------------------------------------

model=joblib.load("/Users/ggharish13/Data Science/Capstone Project/Amazon Music clustering/model.pkl")

# ------------------------------------------------------------------------------------------------------------------------------

if "page" in st.query_params:
    st.session_state.page = st.query_params["page"]

# ------------------------------------------------------------------------------------------------------------------------------

def cal(Pca_transform,target,song_name):
    df=pd.DataFrame({"x": Pca_transform[:, 0].tolist(),
        "y": Pca_transform[:, 1].tolist()})
    df['distance'] = np.sqrt((df['x'] - target[0][0])**2 + (df['y'] - target[0][1])**2)
    nearest_points = df.nsmallest(10, 'distance')

    Song_df=pd.read_csv("prediction_in_original.csv")
    # similarSong=Song_df.iloc[nearest_points.index]
    st.markdown(
        """
        <h4 style='text-align: left; color: #C8A2C8;'><br>
            Here are the 10 songs that are most similar :
        </h4>
        """,
        unsafe_allow_html=True
    )
    for a,b in zip(nearest_points.index,range(1,len(nearest_points.index)+1)):
        st.write(f"{b}. {Song_df.iloc[a]["name_song"]} by {Song_df.iloc[a]["name_artists"]}")

# ------------------------------------------------------------------------------------------------------------------------------


# --- Render selected page ---
if st.session_state.page == "Song Prediction":
    st.markdown(
        """
        <h1 style='text-align: center; color: white;'>
            Discover your song’s genre in just a few steps.
        </h1>
        """,
        unsafe_allow_html=True
    )

    option=st.radio("Press the type of input :",["Song Name", "Manual"],horizontal=True)
    if option=="Manual":
        col1,col2=st.columns(2)
        with col1: 
            song_name_input=st.text_input("Enter the Song Name",)
            song_min=st.text_input("Enter song's length in minute","2")
            Dancibility=st.slider("Dancibility (scale 0-1)",0.0,1.0,0.01)
            Loudness=st.slider("Loudness (scale 0-1)",-50.0,10.0,0.01)
            Acousticness=st.slider("Acousticness (scale 0-1)",0.0,1.0,0.01)
            liveness=st.slider("liveness (scale 0-1)",0.0,1.0,0.01)
            

        with col2: 
            Tempo=st.text_input("Tempo",100)
            song_sec=st.text_input("Enter song's length in seconds","30")
            Energy=st.slider("Energy (scale 0-1)",0.0,1.0,0.01)
            Speechness=st.slider("Speechness (scale 0-1)",0.0,1.0,0.01)
            Instrumentalness=st.slider("Instrumentalness (scale 0-1)",0.0,1.0,0.01)
            Valance=st.slider("Valance (scale 0-1)",0.0,1.0,0.01)

        duration_ms=int((int(song_min)*60+int(song_sec))*1000)
        input_data=np.array([[duration_ms,Dancibility,Energy,Loudness,Speechness,Acousticness,Instrumentalness,liveness,Valance,float(Tempo)]])
        scalar=joblib.load("scalar.pkl")
        scaled_input=scalar.transform(input_data)
        genre_dict={0:"Pop / Dance / Electronic",1:"Acoustic / Ballad / Indie",2:"Rap / Hip-Hop / Spoken-word"}

        if st.button("Identify Genre"):
            prediction_label=model.predict(scaled_input)
            st.markdown(f""" <p style='color:#FFD700;'> With the given song details, we predict that, the song "{song_name_input}" 
                    belongs to "{genre_dict[prediction_label[0]]}" Genre. </p>""", unsafe_allow_html=True)
        

            pca_fit=joblib.load("pca_data_fit.pkl")
            Pca_transform_data=joblib.load("pca_data_transform.pkl")
            pca=pca_fit.transform(scaled_input)

            target_data=pca.tolist()
            st.markdown(
    """
    <h1 style='text-align: center; color: white;'>
        Songs You'll Love Next
    </h1>
    """,
    unsafe_allow_html=True)

            pred=cal(Pca_transform_data,target_data,song_name_input)
                
# ------------------------------------------------------------------------------------------------------------------------------

    elif option=="Song Name":
        df=pd.read_csv("single_genre_artists.csv")
        artist=list(df["name_artists"].unique())
        artist_name_option=st.selectbox("Enter Artist Name :",artist)
        song=df[df["name_artists"]==f"{artist_name_option}"]
        song_list=list(song["name_song"])
        song_name_option=st.selectbox("Enter Song Name :",song_list)
        prediction_df=pd.read_csv("prediction_in_original.csv")
        genre=list(prediction_df[prediction_df["name_song"]==f"{song_name_option}"]["genre"])
        st.write(f"""<p style='color:#FFD700;'> The song '{song_name_option}' predicted as '{genre[0]}'</p> """, unsafe_allow_html=True)

        index_no=df[df["name_song"]==f"{song_name_option}"].index
        pca_data=joblib.load("pca_data_transform.pkl")

        target_data=pca_data[index_no,:]
        st.markdown(
    """
    <h1 style='text-align: center; color: white;'>
        Songs You'll Love Next
    </h1>
    """,
    unsafe_allow_html=True)
        pred=cal(pca_data,target_data,song_name_option)

# ------------------------------------------------------------------------------------------------------------------------------

if st.session_state.page == "Groove by Mood":
    exec(open("Similar_song.py").read())

if st.session_state.page == "Visualizations":
    exec(open("visualization.py").read())

if st.session_state.page == "About":
    exec(open("About.py").read())

# ------------------------------------------------------------------------------------------------------------------------------


page1_footer()