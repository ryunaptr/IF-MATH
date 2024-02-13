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

    st.header("10122247 - Rania Shahinaz")
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
        st.write('Pembelian yang banyak di suatu negara dapat dipengaruhi oleh sejumlah faktor, termasuk stabilitas ekonomi, pertumbuhan pasar, kemudahan berbisnis, demografi yang menguntungkan, infrastruktur yang baik, ketidakstabilan di negara lain, ketersediaan sumber daya alam, dan kebijakan pemerintah yang mendukung investasi dan perdagangan. Kombinasi dari faktor-faktor ini dapat membuat suatu negara menjadi destinasi yang menarik bagi perusahaan untuk melakukan investasi dan berkontribusi pada peningkatan volume pembelian. hal-hal tersebutlah yang membuat suatu negara memiliki banyak member di suatu e-commerce.')

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah
    
    # Ambil 10 kota teratas berdasarkan kolom yang sesuai
    bottom_cities = df_customer['customer_city'].value_counts().tail(5)
    bottom_cities.columns = ['Seller_City','Jumlah']

    Kota_Terbawah = bottom_cities.tail(5)

    st.header("Diagram Banyaknya Member di 10 Kota")
    st.dataframe(Kota_Terbawah)

    # Buat pie chart
    fig, ax = plt.subplots()
    ax.pie(bottom_cities, labels=bottom_cities.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Pastikan pie chart terlihat seperti lingkaran
    
    # Tampilkan pie chart di Streamlit
    st.pyplot(fig)

    
    #Expander Grafik
    with st.expander("Penjelasan Kota dengan Member paling sedikit") :
        st.write('Kota-kota dengan pembelian sangat sedikit cenderung memiliki kondisi ekonomi yang lemah, tingkat pengangguran tinggi, ketidakpastian politik, kurangnya akses ke sumber daya, atau masalah kemiskinan dan kesenjangan ekonomi. Faktor-faktor ini dapat bersama-sama menyebabkan rendahnya daya beli masyarakat dan aktivitas ekonomi di kota tersebut.hal-hal tersebutlah yang membuat kota - kota tersebut kurangnya minat untuk menjadi member di suatu e-commerce.')

def Analisis_Pembayaran(df_payment):
    # Mengelompokkan data pembayaran berdasarkan urutan pembayaran dan menghitung jumlah pembayaran untuk setiap urutan
    payment_by_sequence = df_payment.groupby('payment_sequential')['payment_value'].sum().reset_index()

    st.header("Grafik Urutan Pembayaran")
    st.dataframe(payment_by_sequence)

    # Menampilkan lima baris pertama dari data pembayaran
    print(payment_by_sequence.head())

    payment_by_type = df_payment.groupby('payment_type')['payment_value'].sum().reset_index()
    fig, ax = plt.subplots()
    ax.bar(payment_by_type['payment_type'], payment_by_type['payment_value'], color='blue')
    ax.set_xlabel('Metode Pembayaran')
    ax.set_ylabel('Total Pembayaran')
    plt.title('Analisis Pembayaran Berdasarkan Metode Pembayaran')

    #Menambahkan Label Pada Setiap Bar
    for i in range (len(payment_by_type['payment_type'])) :
        ax.text(payment_by_type['payment_type'][i], payment_by_type['payment_value'][i], str(payment_by_type['payment_value'][i]), ha='center', va='bottom' )

    # Pengelompokkan data pembayaran berdasarkan urutan pembayaran dan menghitung jumlah pembayaran untuk setiap urutan
    payment_by_sequence = df_payment.groupby('payment_sequential')['payment_value'].sum().reset_index()

    # Buat grafik garis
    fig, ax = plt.subplots()
    ax.plot(payment_by_sequence['payment_sequential'], payment_by_sequence['payment_value'], marker='o', linestyle='-')
    ax.set_xlabel('Urutan Pembayaran')
    ax.set_ylabel('Total Pembayaran')
    plt.title('Analisis Pembayaran Berdasarkan Urutan Pembayaran')
    plt.grid(True)
    plt.show()
    
    #Rotasi Label 45 derajat
    plt.xticks(rotation=45)
    plt.show()
     


#Expander Grafik
    with st.expander("Penjelasan Tentang Urutan Pembayaran") :
        st.write('Grafik garis menunjukkan tren jumlah pembayaran berdasarkan urutan pembayaran. Dari grafik tersebut, kita dapat melihat apakah jumlah pembayaran cenderung meningkat, menurun, atau tetap stabil seiring dengan urutan pembayaran. Ini membantu kita dalam memahami perilaku pembayaran pelanggan dan pola yang mungkin ada dalam proses pembayaran.')


    

df_customer = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/customers_dataset.csv")
df_payment = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/order_payments_dataset.csv")
df_item = load_data("https://raw.githubusercontent.com/nianaa24/IF-MATH/main/order_items_dataset.csv")
df_review = load_data("")
df_seller = load_data("")


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
    with tab2 :
        Analisis_Pembayaran(df_payment)
    


