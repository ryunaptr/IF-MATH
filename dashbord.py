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
    count_review_city = df_Review_1['customer_city'].value_counts().reset_index()
    count_review_city.columns = ['Seller_City','Jumlah']
    Lima_Terendah = count_review_city.head()

    #Analisis Data Review Penilaian
    st.header("Grafik Review Terhadap Order Konsumen")
    count_reviews_sorted = count_reviews.sort_values(by='Review_Score')
        
    st.dataframe(count_reviews_sorted)

df_customer = load_data("https://github.com/nianaa24/IF-MATH/blob/main/customers_dataset.csv")

with st.sidebar :
    selected = option_menu('Menu',['Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=0)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis E-Commerce")
    tab1 = st.tabs(["Analisis Pelanggan"])

    with tab1 :
        Analisis_Pelanggan_Unik_Per_Kota(df_customer)
