import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Klasifikasi Kopi",
    page_icon="🧊",
)
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
st.title('Riwayat Klasifikasi Kopi')

st.markdown('<p style="text-align: justify;">Berikut Riwayat dari Klasifikasi Kopi: </p>', unsafe_allow_html=True)


data = pd.read_csv('data/hasil_klasifikasi.csv')

st.table(data)


