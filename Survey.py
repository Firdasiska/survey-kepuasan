import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Kepuasan_walmur.sav','rb'))

st.title('Sistem Kepuasan Wali Murid PT.Lesinaja Edukasi Indonesia')
st.image('logo.png')

st.text('Berikan penilaian Bapak/Ibu sesuai dengan instruksi di bawah ini :')

col1, col2 = st.columns(2)
with col1:
    st.text('1 = Tidak Baik')
    st.text('2 = Kurang Baik')
with col2:
    st.text('3 = Cukup Baik')
    st.text('4 = Baik')


Nama = st.text_input ('Nama Bapak/Ibu')

A1 = st.selectbox (
    'Bagaimana pendapat bapak/ibu mengenai penguasaan materi oleh mentor ketika mengajar?',
    ('Pilih Jawaban', '1', '2', '3', '4'),
)

A2 = st.selectbox (
    'Bagaimana pendapat bapak/ibu mengenai sikap  mentor ketika mengajar?',
    ('Pilih Jawaban', '1', '2', '3', '4'),
)

A3 = st.selectbox (
    'Bagaimana pendapat bapak/ibu mengenai materi yang disampaikan mentor relevan atau tidak dengan pembelajaran di sekolah?',
    ('Pilih Jawaban', '1', '2', '3', '4'),
)

A4 = st.selectbox (
    'Bagaimana pendapat bapak/ibu mengenai waktu pertemuan belajar mentor dengan harga yang ditawarkan sesuai?',
    ('Pilih Jawaban', '1', '2', '3', '4'),
)

A5 = st.selectbox (
    'Bagaimana pendapat bapak/ibu mengenai nilai anak bapak/ibu ketika di sekolah setelah mengikuti bimbel?',
    ('Pilih Jawaban', '1', '2', '3', '4'),
)

predict_satisfaction = ''

if st.button('Lihat Hasil Analisis'):
    satisfaction_predict = model.predict([[A1,A2,A3,A4,A5]])

    if (satisfaction_predict [0]== 0):
        predict_satisfaction = 'Berdasarkan Hasil analisis, hasil survey Anda Tidak Puas'
    else:
        predict_satisfaction = 'Berdasarkan Hasil analisis, hasil survey Anda Puas'
st.success(predict_satisfaction)