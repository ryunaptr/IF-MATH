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

def Analisis_Pelanggan_Unik_Per_Kota(df_customer) :
    count_review_city = df_customer['customer_state'].value_counts().reset_index()
    count_review_city.columns = ['Seller_City','Jumlah']

    Lima_Terendah = count_review_city.head(10)
    
    st.header("Grafik 10 Negara dengan Customer Terbanyak")
    st.dataframe(Lima_Terendah)

    # Buat bar chart
    label = Lima_Terendah['Seller_City']
    data = Lima_Terendah['Jumlah']

    fig, ax = plt.subplots()
    ax.bar(label, data, color=['purple' if jumlah <= 10000 else 'red' for jumlah in data])
    ax.set_xlabel('Seller_City')
    ax.set_ylabel('Jumlah')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(label)) :
        ax.text(label[i], data[i], str(data[i]), ha='center', va='bottom' )

    #Rotasi Label 45 derajat
    plt.xticks(rotation=45)                    
    st.pyplot(fig)

    #Expander Grafik
    with st.expander("Penjelasan Cabang Terendah") :
        st.write('Analisis selanjutnya untuk menambah wawasan pengguna, terlihat terdapat 2 cabang yang memiliki penilaian 1 terbanyak, diantaranya Sao Paulo sebanyak 3.571 dan ibitinga sebangayk 1.241. dari sini perusahaan dapat mengambil keputusan apakah barang dari cabang tersebut perlu di cek kembali kualitasnya atau menutup pengiriman dari cabang tersebut')

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
    
    #Perhitungan value_count() untuk status 'processing','shipped','delivered'
    count_sp = df_customer['customer_city'].value_counts()['sau paolo']
    count_rdj = df_customer['customer_city'].value_counts()['rio de janeiro']
    count_bh = df_customer['customer_city'].value_counts()['belo horizonte']
    count_b = df_customer['customer_city'].value_counts()['brasilia']
    count_cu = df_customer['customer_city'].value_counts()['curitiba']
    count_ca = df_customer['customer_city'].value_counts()['campinas']
    count_pa = df_customer['customer_city'].value_counts()['porto alegre']
    count_s = df_customer['customer_city'].value_counts()['salvador']
    count_g = df_customer['customer_city'].value_counts()['guarulhos']
    count_sbdc = df_customer['customer_city'].value_counts()['sao bernardo do campo']

    data_kota_member_terbanyak = pd.DataFrame({
        'Kategori': ['sau paolo', 'rio de janeiro', 'belo horizonte', 'brasilia', 'curitiba', 'campinas', 'porto alegre', 'salvador', 'guarulhos', 'sao bernardo do campo'],
        'Jumlah': [count_sp,count_rdj,count_bh,count_b,count_cu,count_ca,count_pa,count_s,count_g,count_sbdc]
    })

    df = pd.DataFrame(data_kota_member_terbanyak)

    # Buat pie chart dengan Plotly Express
    fig = px.pie(df, values='Jumlah', names='Kategori', title='Persentasi Member di 10 Kota')
    
    # Tampilkan pie chart menggunakan Streamlit
    st.plotly_chart(fig)
    
    #Expander Grafik
    with st.expander("Penjelasan Cabang Terendah") :
        st.write('Analisis selanjutnya untuk menambah wawasan pengguna')


df_customer = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/customers_dataset.csv")

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1,tab2 = st.tabs(["Analisis Pengiriman", "Analisis Review"])
    
    with tab1 :
        Analisis_Pelanggan_Unik_Per_Kota(df_customer)
    


