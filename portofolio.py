import streamlit as st
from modules import game_istorya, sport_analytics

# Set up the sidebar for navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to",
    ("Home", "Projects")
)

# Function to display the Home page
def show_home():
    
    st.title("My Portofolio")
    
    st.subheader("About Me")
    st.write("""
    Halo! Saya adalah seorang penggemar data yang saat ini berada di tahun kedua menempuh Program Studi Statistika di Universitas Islam Indonesia. Saya memiliki ketertarikan yang kuat pada analisis data, pemrograman (Python, SQL, R), dan visualisasi data menggunakan tools seperti Tableau dan Matplotlib.
    """)
    
    st.markdown("### Core Skills")
    st.write("""
    - 💻 **Programming Language**: Python (Pandas, NumPy, Matplotlib), SQL (MySQL), R (dplyr, ggplot, tidyr)
    - 📊 **Data Tools**: Ms. Excel, RStudio
    - 📈 **Data Vizualitation**: Tableau
    """)
    
    st.markdown("### Contact Me")
    st.write("Feel free to reach out to me through the following platforms:")
    st.write("""
    - **Email**: hilalaf0520@gmail.com
    - **LinkedIn**: [LinkedIn Profile](https://linkedin.com/in/hilal-azhar-fawaz-139739284)
    - **GitHub**: [GitHub Profile](https://github.com/azharhf)
    """)
    
    st.markdown("### Download CV")
    with open("assets/cv.pdf", "rb") as file:
        st.download_button(
            label="My CV",
            data=file,
            file_name="Hilal_Azhar_Fawaz_CV.pdf",
            mime="application/pdf",
            key="download_cv_button",
            help="Klik untuk mengunduh CV saya."
        )

# Function to display the Projects page
def show_projects():
    project_menu = st.sidebar.selectbox(
        "Select a project",
        ("Game ISTORYA", "Sport Analytics")
    )
    
    if project_menu == "Game ISTORYA":
        game_istorya.show_gi()
    elif project_menu == "Sport Analytics":
        sport_analytics.show_sa()
        
# Logic to display the selected page based on sidebar radio
if menu == "Home":
    show_home()
elif menu == "Projects":
    show_projects()

# Setting color and font
st.markdown(
    """
    <style>
    .css-18e3th9 {
        font-family: 'Arial', sans-serif;
        color: #333333;
    }
    .css-1d391kg {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
