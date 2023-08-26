# Capstone-Project-M3
Capstone project ini bertujuan untuk membuat model prediksi harga apartemen Daegu

- **Model Deployment Streamlit** -> [link](https://capstone-project-m3-cixmbn7dmsfmgpud6ytz5x.streamlit.app/)
- **Presentasi** -> [link](https://drive.google.com/drive/folders/1Ni71YrJY8iD9mTspXsFcN4phcT9Fio6V?usp=sharing)

# Business Understanding:
Peningkatan kebutuhan tempat tinggal di kota metropolitan kadang menjadi masalah, karena banyak individu yang beraktivitas di kota metropolitan dan membutuhkan tempat tinggal di sekitar kota untuk kemudahan beraktivitas.

Sebagai perusahaan properti kondisi tersebut dapat menjadi peluang bisnis. Perusahan XYZ merupakan perusahaan properti khususnya apertemen di Korea. Perusahaan tersebut biasanya melakukan jual beli apartemen. Kebanyakan apartemen yang dibeli akan dijual kembali. Dalam proses pembelian apertemen, perusahaan biasanya menyewa jasa (pihak ke-3) untuk pengecekan harga apartemen, hal tersebut dilakukan untuk survey harga serta  membandingkan harga apartemen yang akan dibeli. Dalam penjualan apartemen, proses penetepan harga apartemen dilakukan oleh divisi di perusahaan. 

- Masalah:
  - proses survey harga apartemen dirasa oleh perusahaan kurang efisien, karena perlu mengeluarkan biaya tambahan dalam menyewa jasa survey, hal tersebut juga dapat menggerus keuntungan saat akan menjual apartemen yang teleh dibeli.
  - penentuan harga apartemen kadang menghasilkan harga apartemen yang underpriced atau overpriced. Harga jual overpriced bisa menyebakan apartemen tidak laku karena harga kalah saing di pasaran, sedangkan harga jual yang underpriced menyebabkan keuntungan yang didapat tidak maksimal.

- Tujuan: Berdasarkan permasalahan di atas,  perusahaan memerlukan model yang dapat menaksir harga apartemen sehingga tidak perlu menggunakan pihak ke-3, selain dari itu model juga dapat membantu perusahaan untuk menentukan harga apartemen yang dijual sehingga tidak underpriced atau overpriced.

- Analisis: Oleh karena itu, perlu dilakukan analisis untuk data apartemen, mulai dari harga sampai ke karakteristik apartemen yang dapat mempengaruhi harga. Selanjutnya membangun model menggunakan machine learning khususnya regresi karena akan memprediksi harga apartemen, sehingga diharapkan dapat membantu perusahaan saat membandingkan harga apartemen yang akan dibeli dan saat menetapkan harga apartemen untuk dijual.

- Metrik evaluasi : MAE, MAPE, dan MSLE

# Data Understanding

|No|Nama Variabel|Deskripsi
|---|---|---|
|1|HallwayType|tipe apartemen
|2|TimeToSubway|waktu yang dibutuhkan untuk pergi ke stasiun terdekat
|3|SubwayStation|nama stasiun terdekat
|4|N_FacilitiesNearBy(ETC)|jumlah fasilitas terdekat
|5|N_FacilitiesNearBy(PublicOffice)|jumlah fasilitas publik terdekat
|6|N_SchoolNearBy(University)|jumlah universitas terdekat|
|7|N_Parkinglot(Basement)|jumlah tempat parkir|
|8|YearBuilt|tahun apartemen dibangun|
|9|N_FacilitiesInApt|jumlah fasilitas di apartemen|
|10|Size(sqf)|luas apartemen|
|11|SalePrice|harga apartemen (won)|

- Setiap baris merepresentasikan unit apartemen yang ada
- Terdapat temuan proporsi data duplikat sebanyak 34%
- Hanya 2 variabel numerik yang memiliki outlier dengan proporsi yang sedikit
- Seluruh variabel numerik tidak berdistribusi normal
- Terdapat masalah multikolinearitas

# Data Preparation
- Handling Outlier : Outlier tidak dibuang
- Feature selection : Terdapat variabel yang dibuang berdasarkan domain knowledge dan nilai vif
- Encoding : Ordinal dan one hot encoding

# Data Analysis
Memvisualisasikan proprosi apartemen berdasarkan karakteristik yang dimiliki, serta mencari jenis apartemen yang harganya paling mahal dan ukurannya besar

# Modeling & Evaluation
- Menggunakan 9 algoritma yaitu linreg, lasso, ridge, knn, decision tree, random forest, SVR, gradient boosting serta XGB
- Terdapat pemodelan dengan mentransformasi target variabel
- Metrik yang digunakan adalah MAE, MAPE dan MSLE
- Tuning XGBRegressor
- Model terbaik adalah XGBRegressor tuning dengan mentransformasi variabel target
- Analisis hasil prediksi dan residual
- Feature importance
  
# Kesimpulan & Rekomendasi 
- Model terbaik adalah XGB Regressor Tuning with TTR
- Model dapat memprediksi harga apartemen +- 31572 won atau error 16.7% dari harga aslinya.
- Feature importance = HallwayType, N_FacilitiesInApt, N_FacilitieseNearBy(ETC), Size(sqf), YearBuilt
- Terdapat limitasi model berdasarkan statistika deskriptif serta sebaran data residual dan prediksi

Rekomendasi model:
- Mencari fitur yang lebih menggambarkan harga, sehingga tidak terindikasi sebagai data duplikat
- Pemodelan dan hyperparameter tuning ulang berdasarkan feature imporatance
- Mencari data apartemen mahal, sehingga target variabel tidak skewness
- Melakukan update data

Rekomendasi Perusahaan:
- Melakukan prediksi harga yang akan dibeli mengggunakan model, sehingga meminimalisir pengeluaran
- Menggunakan model sebagai bantuan dalam proses penetapan harga

# Deployment
Pengaplikasian model yang telah dibuat menggunakan streamlit

