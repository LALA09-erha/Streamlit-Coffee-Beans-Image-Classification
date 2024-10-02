# inisialisasi library
import streamlit as st
import pandas as pd

# judul website
st.set_page_config(
    page_title="Klasifikasi Kopi",
    page_icon="🧊",
)
st.title('Website Klasifikasi Kopi')

# ambil [data-testid="stSidebarNavLink"] yang pertama dari sidebar
st.markdown("""
<style>
            
[data-testid="stSidebarNavLink"] {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    padding: 10px;
    border-radius: 10px;
    color: black;
    text-transform: capitalize;
}
</style>
""", unsafe_allow_html=True)
# change name of menu like name of this file in sidebar just in this page


#penjelasan Kopi 

st.markdown('<div style="text-align: justify;"> <b>Coffee Bean:</b> Biji kopi adalah biji yang berasal dari tanaman kopi, yang termasuk dalam genus Coffea. Dua jenis biji kopi yang paling populer adalah Arabika (Coffea arabica) dan Robusta (Coffea canephora). Biji kopi melalui proses pemetikan, pengeringan, pemanggangan, hingga penggilingan sebelum menjadi bubuk kopi yang siap diseduh. Karakteristik biji kopi seperti rasa, aroma, keasaman, dan kekuatan dipengaruhi oleh berbagai faktor seperti varietas tanaman, lingkungan tumbuh, dan metode pengolahan. Biji kopi memiliki nilai komersial tinggi dan menjadi komoditas penting dalam perdagangan internasional.</div>', unsafe_allow_html=True)

st.text("")

# penjelasan SVM
st.markdown('<div style="text-align: justify;">CNN (Convolutional Neural Network): CNN, atau Convolutional Neural Network, adalah jenis jaringan saraf tiruan yang dirancang untuk memproses data berstruktur grid seperti gambar. CNN digunakan secara luas dalam pengenalan gambar dan analisis visual karena kemampuannya dalam menangkap fitur spasial dan pola dalam data gambar. CNN terdiri dari beberapa lapisan, termasuk lapisan konvolusi, lapisan pooling, dan lapisan fully connected. Setiap lapisan memiliki fungsi spesifik dalam mengekstrak dan mengabstraksi fitur dari gambar input, yang kemudian digunakan untuk mengklasifikasikan atau mengenali objek dalam gambar tersebut. CNN telah menunjukkan kinerja luar biasa dalam berbagai aplikasi, termasuk pengenalan wajah, diagnosis medis, dan klasifikasi objek.</div>', unsafe_allow_html=True)

st.text("")

# data
st.markdown('<h5>Beberapa sample terkait data yang digunakan dalam penelitian ini: </h5>', unsafe_allow_html=True)

images = ['https://pbs.twimg.com/media/GSnAm-nbIAErT7o?format=png&name=240x240','https://pbs.twimg.com/media/GSnAm-nbIAErT7o?format=png&name=240x240', 'https://pbs.twimg.com/media/GSnAoU7acAA5-Zd?format=png&name=240x240','https://pbs.twimg.com/media/GSnAoU7acAA5-Zd?format=png&name=240x240', 'https://pbs.twimg.com/media/GSnApmPbIAcQEvl?format=png&name=240x240','https://pbs.twimg.com/media/GSnArB6bIAELtvt?format=png&name=240x240']
st.image(images, use_column_width=False, caption=["Dark","Dark", "Green","Green","Light", "Medium"])
# show data with dataframe table mengambil 10 data pertama

st.markdown('<h5>Dataset Terdapat Beberapa Kelas Antara Lain : Dark, Green, Light, Medium </h5>', unsafe_allow_html=True)
