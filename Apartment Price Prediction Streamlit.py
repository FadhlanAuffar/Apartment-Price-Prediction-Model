import streamlit as st
import pandas as pd
import pickle
from PIL import Image

st.image(Image.open('Fig 1.jpeg'))

st.title('Capstone Project Module 3: Model Deployment')
st.title('A. Daegu Apartment Price Prediction')
st.text('Silahkan masukan fitur apartemen yang harganya akan diprediksi')

if 'model' not in st.session_state:
    model = pickle.load(open('Apartment Model.sav', 'rb'))
    st.session_state['model'] = model

HallwayType = st.selectbox(
    '1. Tipe apartemen',
    ('corridor', 'mixed', 'terraced'))

st.write('Tipe apartemen adalah', HallwayType)
st.write('---')


TimeToSubway = st.selectbox(
    '2. Waktu tempuh ke subway terdekat',
    ('0-5min', '10min~15min', '15min~20min', '5min~10min', 'no_bus_stop_nearby'))

st.write('Waktu tempuh ke subway terdekat adalah', TimeToSubway)
st.write('---')


SubwayStation = st.selectbox(
    '3. Subway terdekat',
    ('Bangoge', 'Banwoldang', 'Chil-sung-market', 'Daegu', 'Kyungbuk_uni_hospital', 'Myung-duk', 'Sin-nam', 'no_subway_nearby'))

st.write('Subway terdekat adalah', SubwayStation)
st.write('---')


N_FacilitiesNearBy = st.number_input('4. Masukan jumlah fasilitas terdekat', value = 0, step=1)

if N_FacilitiesNearBy > 5 or N_FacilitiesNearBy < 0:
    st.write('Masukan rentang nilai dari 0-5, apabila nilai di luar rentang hasil prediksi menjadi tidak akurat')
    st.write('---')
else :
    st.write('Jumlah fasilitas terdekat dari apartemen adalah', N_FacilitiesNearBy)
    st.write('---')


YearBuilt = st.selectbox(
    '5. Tahun apartemen dibangun',
    ('1978', '1980', '1985', '1986', '1992', '1993', '1997', '2003', '2005', '2006', '2007', '2008', '2009', '2013', 2014, 2015))

st.write('Tahun apartemen dibangun adalah', YearBuilt)
st.write('---')


N_FacilitiesInApt = st.number_input('6. Masukan jumlah fasilitas di apartemen', value = 1, step=1)

if N_FacilitiesInApt > 10 or N_FacilitiesInApt < 1:
    st.write('Masukan rentang nilai dari 1-10, apabila nilai di luar rentang hasil prediksi menjadi tidak akurat')
    st.write('---')
else :
    st.write('Jumlah fasilitas di apartemen adalah', N_FacilitiesInApt)
    st.write('---')

Size = st.number_input('7. Masukan jumlah luas apartemen (sqf)', value = 135)
if Size < 135 or Size > 2337:
    st.write('Masukan rentang nilai dari 135 - 2337, apabila nilai di luar rentang hasil prediksi menjadi tidak akurat')
    st.write('---')
else :
    st.write('Luas apartemen adalah', Size)
    st.write('---')


st.title('B. Rekap Data Input')
rekap = pd.DataFrame()
rekap['HallwayType'] = [HallwayType]
rekap['TimeToSubway'] = [TimeToSubway]
rekap['SubwayStation'] = [SubwayStation]
rekap['N_FacilitiesNearBy(ETC)'] = [N_FacilitiesNearBy]
rekap['YearBuilt'] = [YearBuilt]
rekap['N_FacilitiesInApt'] = [N_FacilitiesInApt]
rekap['Size(sqf)'] = [Size]

st.dataframe(data=rekap)

st.title('C. Prediksi')
if st.button('Prediksi harga apartemen'):

    if N_FacilitiesNearBy < 0 or N_FacilitiesInApt < 0 or Size < 0:
        st.write('Nilai fitur tidak bisa negatif')
    else:
        hasil = st.session_state['model'].predict(rekap)
        st.write(f'Hasil prediksi harga apartemen adalah {round(hasil[0])} won')
else:
    st.write('Masukan nilai fitur apartemen')