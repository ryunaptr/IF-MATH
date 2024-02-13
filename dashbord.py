import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu


@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def Analisis_Pelanggan(df_customer) :
    count_customer_state = df_customer['customer_state'].value_counts().reset_index()
    count_customer_state.columns = ['Negara','Jumlah']

    Negara_Teratas = count_customer_state.head(10)
    
    st.header("Grafik 10 Negara dengan Customer Terbanyak")
    st.dataframe(Negara_Teratas)

    # Buat bar chart
    label = Negara_Teratas['Negara']
    data = Negara_Teratas['Jumlah']

    fig, ax = plt.subplots()
    ax.bar(label, data, color=['purple' if jumlah <= 10000 else 'red' for jumlah in data])
    ax.set_xlabel('Negara')
    ax.set_ylabel('Jumlah')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(label)) :
        ax.text(label[i], data[i], str(data[i]), ha='center', va='bottom' )

    #Rotasi Label 45 derajat
    plt.xticks(rotation=45)                    
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Negara dengan Member Terbanyak") :
        st.write('Analisis selanjutnya untuk menambah wawasan pengguna, terlihat terdapat 2 cabang yang memiliki penilaian 1 terbanyak, diantaranya Sao Paulo sebanyak 3.571 dan ibitinga sebangayk 1.241. dari sini perusahaan dapat mengambil keputusan apakah barang dari cabang tersebut perlu di cek kembali kualitasnya atau menutup pengiriman dari cabang tersebut')

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
    
    # Ambil 10 kota teratas berdasarkan kolom yang sesuai
    bottom_cities = df_customer['customer_city'].value_counts().tail(5)
    bottom_cities.columns = ['Seller_City','Jumlah']

    Kota_Terbawah = bottom_cities.tail(5)

    st.header("Diagram Banyaknya Member di 10 Kota")
    st.dataframe(Kota_Terbawah)

    # Buat pie chart
    fig, ax = plt.subplots()
    ax.pie(top_cities, labels=top_cities.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Pastikan pie chart terlihat seperti lingkaran
    
    # Tampilkan pie chart di Streamlit
    st.pyplot(fig)

    
    #Expander Grafik
    with st.expander("Penjelasan Kota dengan Member paling sedikit") :
        st.write('Analisis selanjutnya untuk menambah wawasan pengguna')


df_customer = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/customers_dataset.csv")

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1,tab2 = st.tabs(["Analisis Pelanggan", "Analisis Review"])
    
    with tab1 :
        Analisis_Pelanggan(df_customer)
    


