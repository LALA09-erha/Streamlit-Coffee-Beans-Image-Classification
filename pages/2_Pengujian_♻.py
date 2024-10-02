import streamlit as st
import controller.prosesklasifikasi as pk
import pandas as pd
import time


# judul halaman
st.set_page_config(
    page_title="Uji Coba",
    page_icon="🧊",
)
st.title('Uji Data Menggunakan Model Terbaik')

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

uploaded_files = st.file_uploader("Upload Image Coffe", type=['png', 'jpg', 'jpeg'])




columns = st.columns((2, 0.6, 2))
sumbit = columns[1].button("Submit")



# jika tombol submit ditekan
if sumbit == True and uploaded_files is not None:            
        # print(uploaded_files)
        # prediksi
        hasil = pk.cnn(uploaded_files)
        # buatkan load sebelum hasil ada
        while hasil is None:
            st.spinner('Wait for it...')
        st.success(f"Hasil Klasifikasi Kopi Di bawah Adalah : {hasil}")
        
        # dapatkan nama file tanpa ekstensi
        nama_file = uploaded_files.name.split('.')[0]
        # dapatkan tanggal dan waktu upload
        waktu_upload = time.strftime('%Y-%m-%d %H:%M:%S')
        # simpan nama, waktu, dan hasil klasifikasi ke dalam dataframe
        df = pd.DataFrame({'Nama File': [nama_file], 'Waktu Upload': [waktu_upload], 'Hasil Klasifikasi': [hasil]})
        
        # ambil data dari file csv
        data = pd.read_csv('data/hasil_klasifikasi.csv')
        # jika file csv kosong
        if data.empty:
            # simpan data ke dalam file csv
            df.to_csv('data/hasil_klasifikasi.csv', index=False, columns=['Nama File', 'Waktu Upload', 'Hasil Klasifikasi'])
        else:
            # simpan data ke dalam file csv
            data = data._append(df, ignore_index=True)
            data.to_csv('data/hasil_klasifikasi.csv', index=False, columns=['Nama File', 'Waktu Upload', 'Hasil Klasifikasi'])

        
        
        st.image(uploaded_files, use_column_width=True)
else:
    st.warning("Silahkan Upload Gambar")