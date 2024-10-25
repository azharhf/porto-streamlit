import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Fungsi Utama
def show_sa():
    st.title("Analisis Pertandingan Ginting VS Antonsen")
    st.write(""" 
    - **Deskripsi**: Analisis ini dilakukan dengan mengamati dan mencatat secara mendetail setiap gerakan Anthony Sinisuka Ginting dan Anders Antonsen selama pertandingan di KFF Singapore Open 2023. 
    Pengamatan dilakukan dengan metode pengkodean yang meliputi jenis pukulan, arah pukulan, serta posisi pemain. Data ini kemudian dianalisis untuk mengevaluasi strategi permainan masing-masing pemain.
    
    - **Sumber Tontonan** : Pertandingan dapat ditonton melalui [FINAL KFF SINGAPORE OPEN 2023 : Anders Antonsen (DEN) vs. Anthony Sinisuka Ginting (INA)](https://www.youtube.com/live/CgMHgZ6ONTA?si=HCHmrmcF3mckRdv9)
    """)

    variables = {
        "Jenis Pukulan": {
            'Jenis Pukulan': ['Tidak Ada Aksi', 'Servis Pendek', 'Servis Panjang', 'Servis Flick', 'Servis Fault', 
                              'Smash Forehand', 'Smash Backhand', 'Lob', 'Dropshot', 'Drive', 'Netting', 'Fault'],
            'ID': list(range(0,12))
        },
        "Arah Pukulan": {
            'Arah Pukulan': ['Tidak Ada Aksi', 'Kanan Depan Lapangan', 'Tengah Depan Lapangan', 
                        'Kiri Depan Lapangan', 'Tengah Lapangan', 'Kanan Belakang Lapangan', 
                        'Tengah Belakang Lapangan', 'Kiri Belakang Lapangan'],
            'ID': list(range(0,8))
        },
        "Posisi": {
            'Posisi': ['Tidak Ada Aksi', 'Kanan Depan Lapangan', 'Tengah Depan Lapangan', 
                        'Kiri Depan Lapangan', 'Tengah Lapangan', 'Kanan Belakang Lapangan', 
                        'Tengah Belakang Lapangan', 'Kiri Belakang Lapangan'],
            'ID': list(range(0,8))
        },
        "Keputusan": {
            'Keputusan': ['In','Out'],
            'ID': [1,2]
        }
    }

    column_mapping = {
        'Jenis Pukulan Ginting': 'Jenis Pukulan',
        'Arah Pukulan Ginting': 'Arah Pukulan',
        'Posisi1 Ginting': 'Posisi',
        'Posisi2 Ginting': 'Posisi',
        'Jenis Pukulan Antonsen': 'Jenis Pukulan',
        'Arah Pukulan Antonsen': 'Arah Pukulan',
        'Posisi1 Antonsen': 'Posisi',
        'Posisi2 Antonsen': 'Posisi'
    }
    # Dropdown untuk memilih deskripsi variabel
    selected_desc = st.selectbox(
        "**Pengkodean Untuk Masing-Masing Variabel**",
        ["Pilih Keterangan Variabel"] + list(variables.keys())
    )
    
    # Menampilkan tabel sesuai pilihan
    if selected_desc != "Pilih Keterangan Variabel":
        df_selected = pd.DataFrame(variables[selected_desc])
        df_selected.index += 1
        df_selected.index.name = "No"
        
        st.dataframe(df_selected, use_container_width=True)

    # Membaca dataset
    data_mentah = pd.read_excel("data/data_mentah.xlsx", sheet_name=None)
    sheet_names = ['Pilih Data'] + list(data_mentah.keys())

    #Membuat pilihan set pertandingan
    selected_sheet = st.sidebar.selectbox("Pilih Set Pertandingan", sheet_names)

    if selected_sheet != 'Pilih Data':
        df = data_mentah[selected_sheet]
        st.write(f"**Hasil Pengamatan Pertandingan Pada {selected_sheet}**")
        st.dataframe(df)

        paired_columns = {
            "Jenis Pukulan": ['Jenis Pukulan Ginting', 'Jenis Pukulan Antonsen'],
            "Arah Pukulan": ['Arah Pukulan Ginting', 'Arah Pukulan Antonsen'],
            "Posisi1": ['Posisi1 Ginting', 'Posisi1 Antonsen'],
            "Posisi2": ['Posisi2 Ginting', 'Posisi2 Antonsen']
        }

        selected_variable = st.sidebar.selectbox(
            "Hasil Analisis",
            ["Pilih Hasil Analisis", "Jenis Pukulan", "Arah Pukulan", "Posisi1", "Posisi2"]
        )
        
        # Menambahkan menu pilihan jenis visualisasi
        chart_type = st.sidebar.selectbox(
            "Pilih Jenis Visualisasi",
            ['Barplot']
        )

        if selected_variable in paired_columns:
            ginting_col, antonsen_col = paired_columns[selected_variable]

            if ginting_col in df.columns and antonsen_col in df.columns:
                all_ids = variables[column_mapping[ginting_col]]['ID']
                labels = variables[column_mapping[ginting_col]][column_mapping[ginting_col]]

                # Hitung kemunculan untuk Ginting dan Antonsen
                ginting_counts = df[ginting_col].value_counts(dropna=False).reindex(all_ids, fill_value=0).sort_index()
                antonsen_counts = df[antonsen_col].value_counts(dropna=False).reindex(all_ids, fill_value=0).sort_index()

                populasi = ginting_counts.values + antonsen_counts.values
                populasi = np.where(populasi == 0, 1, populasi)

                ginting_percentage = round((ginting_counts / populasi) * 100, 0)
                antonsen_percentage = round((antonsen_counts / populasi) * 100, 0)

                result_df = pd.DataFrame({
                    'ID': all_ids,
                    'Deskripsi': labels,
                    'Ginting': ginting_counts.values,
                    'Antonsen': antonsen_counts.values
                }).reset_index(drop=True)

                result_df.index += 1
                result_df.index.name = "No"

                st.write(f"**Penghitungan {selected_variable} Untuk Tiap Pemain**")
                st.dataframe(result_df, use_container_width=True)

                # Visualisasi berdasarkan pilihan
                if chart_type == 'Barplot':
                    # Barplot horizontal
                    fig = go.Figure()
                    fig.add_trace(go.Bar(
                        y=labels,
                        x=ginting_percentage,
                        name='Ginting',
                        marker_color='blue',
                        hoverinfo='text',
                        hovertext=[f'Ginting: {perc}%' for perc in ginting_percentage],
                        orientation='h'
                    ))
                    fig.add_trace(go.Bar(
                        y=labels,
                        x=antonsen_percentage,
                        name='Antonsen',
                        marker_color='red',
                        hoverinfo='text',
                        hovertext=[f'Antonsen: {perc}%' for perc in antonsen_percentage],
                        orientation='h'
                    ))
                    fig.update_layout(
                        barmode='stack',
                        title={
                            'text': f'Perbandingan {selected_variable} Ginting vs Antonsen',
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
                        },
                        yaxis_title=selected_variable,
                        xaxis_title='Persentase (%)',
                        yaxis=dict(autorange="reversed"),
                        legend=dict(
                            x=1,
                            y=0.5,
                            orientation='v'
                        ),
                        template='plotly_white',
                        transition_duration=500
                    )
                    st.write(f"**Visualisasi {selected_variable} - Barplot**")
                    st.plotly_chart(fig, use_container_width=True)

# Memanggil fungsi utama
if __name__ == "__main__":
    show_sa()
