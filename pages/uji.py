import streamlit as st
import controller.prosesklasifikasi as pk


# judul halaman
st.set_page_config(
    page_title="Uji Coba",
    page_icon="🧊",
)
st.title('Uji Data Menggunakan Model Terbaik')


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
        st.image(uploaded_files, use_column_width=True)
else:
    st.warning("Silahkan Upload Gambar")