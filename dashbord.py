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
     kota_list = ['sau paolo', 'rio de janeiro', 'belo horizonte', 'brasilia', 'curitiba', 'campinas', 'porto alegre', 'salvador', 'guarulhos', 'sao bernardo do campo']
    
    count_review_city = df_customer[df_customer['customer_city'].isin(kota_list)].value_counts()
    
    Lima_Terendah = count_review_city.head(10)

    st.header("Persentase Pelanggan ID Unik per Kota")
    st.dataframe(Lima_Terendah)


    # Buat bar chart
    label = Lima_Terendah['Seller_City']
    data = Lima_Terendah['Jumlah']

    fig, ax = plt.subplots()
    ax.pie(Lima_Terendah, label=Lima_Terendah.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Mengatur aspek rasio agar lingkaran tampak sempurna

    st.pyplot(fig)

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
    


