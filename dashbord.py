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

    st.header("Grafik Ketepatan Jasa Pengiriman")


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
    


