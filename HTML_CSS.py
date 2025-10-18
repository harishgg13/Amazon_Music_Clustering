import streamlit as st
# --------------------------------------------------------------------------------------------------------------------------------------

def page1_home():

    st.markdown(f"""
        <style>
            /* Hide default Streamlit header and footer */
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
                
            .custom-header {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background-color: #413e85;
                color: white;
                font-size: 20px;
                font-weight: bold;
                padding: 5px 20px;
                border-bottom: 1px solid #31333F;
                display: flex;
                align-items: center;
                justify-content: space-between;
                z-index: 1000;
            }}
            .custom-header img {{
                height: 50px;
                vertical-align: middle;
            }}
            .title-group {{
                display: flex;
                align-items: baseline;
                gap: 5px;
            }}
            .beta-text {{
                position: fixed;
                padding: 5px 225px;
                font-size: 15px;
                font-weight: normal;
                color: white;
                font-style: italic;
            }}
            .menu {{
                display: flex;
                gap: 20px;
            }}
            .menu button {{
                background: none;
                border: none;
                color: white;
                font-size: 18px;
                cursor: pointer;
            }}
            .menu button:hover {{
                text-decoration: underline;
            }}
            /* Push content below fixed header */
            .block-container {{
                padding-top: 75px;
            }}
        </style>

        <div class="custom-header">
            <div style="display:flex;align-items:center;gap:10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/d/de/Amazon_icon.png?20171005153412" alt="Logo">
                <div class="title-group">
                    Amazon Music Clustering
                    <span class="beta-text">| Capestone Project Four</span>
                </div>
            </div>
            <div class="menu">
                <form action="" method="get">
                    <button name="page" value="Song Prediction">Song Prediction</button>
                    <button name="page" value="Groove by Mood">Groove by Mood</button>
                    <button name="page" value="Visualizations">Visualizations</button>
                    <button name="page" value="About">About</button>
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
        <style>
            html, body {
                background-image: url("https://i.pinimg.com/736x/6c/bb/36/6cbb36a34afe45944dc1280aed5f9c0c.jpg");
            }
            .stApp {
                background-image: url("https://i.pinimg.com/736x/6c/bb/36/6cbb36a34afe45944dc1280aed5f9c0c.jpg");
                background-repeat: no-repeat;             /* stops tiling */
                background-size: cover;                   /* scales to fill screen */
                background-position: center;              /* centers the image */
                background-attachment: fixed;   
            }
            .block-container {
                background-color: transparent;
            }
        </style>
        
                
    """, True)

# --------------------------------------------------------------------------------------------------------------------------------------

def page2():

    st.markdown(f"""
        <style>
            /* Hide default Streamlit header and footer */
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            header {{visibility: hidden;}}
                
            .custom-header {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background-color: #413e85;
                color: white;
                font-size: 20px;
                font-weight: bold;
                padding: 5px 20px;
                border-bottom: 1px solid #31333F;
                display: flex;
                align-items: center;
                justify-content: space-between;
                z-index: 1000;
            }}
            .custom-header img {{
                height: 50px;
                vertical-align: middle;
            }}
            .title-group {{
                display: flex;
                align-items: baseline;
                gap: 5px;
            }}
            .beta-text {{
                position: fixed;
                padding: 5px 225px;
                font-size: 15px;
                font-weight: normal;
                color: white;
                font-style: italic;
            }}
            .menu {{
                display: flex;
                gap: 20px;
            }}
            .menu button {{
                background: none;
                border: none;
                color: white;
                font-size: 18px;
                cursor: pointer;
            }}
            .menu button:hover {{
                text-decoration: underline;
            }}
            /* Push content below fixed header */
            .block-container {{
                padding-top: 75px;
            }}
        </style>

        <div class="custom-header">
            <div style="display:flex;align-items:center;gap:10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/d/de/Amazon_icon.png?20171005153412" alt="Logo">
                <div class="title-group">
                    Amazon Music Clustering
                    <span class="beta-text">| Capestone Project One</span>
                </div>
            </div>
            <div class="menu">
                <form action="" method="get">
                    <button name="page" value="Song Prediction">Song Prediction</button>
                    <button name="page" value="Similar Songs">Similar Songs</button>
                    <button name="page" value="Visualizations">Visualizations</button>
                    <button name="page" value="About">About</button>
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
        <style>
            html, body {
                background-image: url("https://i.pinimg.com/736x/6c/bb/36/6cbb36a34afe45944dc1280aed5f9c0c.jpg");
            }
            .stApp {
                background-image: url("https://i.pinimg.com/736x/6c/bb/36/6cbb36a34afe45944dc1280aed5f9c0c.jpg");
                background-repeat: no-repeat;             /* stops tiling */
                background-size: cover;                   /* scales to fill screen */
                background-position: center;              /* centers the image */
                background-attachment: fixed;   
            }
            .block-container {
                background-color: transparent;
            }
        </style>
        
                
    """, True)

# --------------------------------------------------------------------------------------------------------------------------------------

def page1_footer():
    
    st.markdown(
        """
        
        <style>
            
            .footer {
                position: fixed;
                bottom: 0;
                left: 0rem; 
                right:0rem;
                width: calc(100%); 
                background-color: #413a85; 
                text-align: center;
                font-size: 12px;
                color: #ffffff;
                padding: 4px 0;
                border-top: 1px solid #333333;
            }
            .footer a {
                color: #aaaaaa; /* links */
                text-decoration: none;
                font-weight: 500;
            }
            .footer a:hover {
                color: #ffffff;
                text-decoration: underline;
            }
            
        </style>
        <div class="footer">
            <b>Youtube Content Monetization</b> | Developed by <b>G G Harish</b> | E-Mail: 
            <a href="mailto:harishgg03@gmail.com" target="_blank">Harishgg03@gamil.com</a> 
        </div>
        """,
        unsafe_allow_html=True
    )


    