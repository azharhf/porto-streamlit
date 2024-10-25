import streamlit as st

# Fungsi Utama
def show_gi():
    st.markdown(
        """
        <h1 style='text-align: center;'>ISTORYA</h1>
        """,
        unsafe_allow_html=True
    )
    # Menampilkan cover istorya
    st.image("assets/COVER_ISTORYA.png", caption="ISTORYA - Indonesian History Adventure", use_column_width=True)
    
    # CSS
    st.markdown(
        """
        <style>
        .center-button {
            display: flex;
            justify-content: center;
        }
        a > button {
            background-color: rgba(255, 255, 0, 0.3);
            color: white;
            border: none;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.3s;
        }
        a > button:hover {
            background-color: rgba(255, 255, 0, 0.7); 
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Tombol
    st.markdown('<div class="center-button"><a href="https://hilalaf.itch.io/istorya" target="_blank"><button>Akses Game ISTORYA</button></a></div><br>', unsafe_allow_html=True)
    
    # Deskripsi game
    st.write(""" 
    - **Deskripsi**: ISTORYA adalah game edukasi sejarah seputar penjajahan Jepang di Indonesia dengan konsep belajar yang kreatif & inovatif
    - **Software** : Construct 3
    """)

# Memanggil fungsi utama
if __name__ == "__main__":
    show_gi()
