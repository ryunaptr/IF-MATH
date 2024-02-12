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
    count_review_city = df_customer['customer_city'].value_counts().reset_index()
    count_review_city.columns = ['Seller_City','Jumlah']
    
    Lima_Terendah = count_review_city.head()

    t.header("Grafik 5 Cabang Terendah")
    st.dataframe(Lima_Terendah)

    # Buat bar chart
    label = Lima_Terendah['Seller_City']
    data = Lima_Terendah['Jumlah']

    fig, ax = plt.subplots()
    ax.bar(label, data, color=['skyblue' if jumlah <= 999 else 'red' for jumlah in data])
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
        st.write('Analisis selanjutnya untuk menambah wawasan pengguna


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
    


