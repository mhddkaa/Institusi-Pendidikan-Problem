# Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut adalah salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik dalam menghasilkan lulusan berkualitas. Namun, institusi menghadapi tantangan serius berupa tingginya angka siswa yang tidak menyelesaikan pendidikan (*dropout*). 

Jumlah *dropout* yang tinggi ini tentu berdampak pada penurunan reputasi dan akreditasi institusi, menurunnya kepercayaan masyarakat, hingga inefisiensi dalam pengelolaan sumber daya pendidikan. Untuk itu, institusi berupaya mendeteksi siswa yang berpotensi mengalami *dropout* lebih awal, sehingga dapat diberikan bimbingan khusus kepada siswa. 

### Permasalahan Bisnis
Berdasarkan kebutuhan pengguna (pihak institusi), terdapat beberapa pertanyaan bisnis yang ingin dijawab melalui analisis data sebagai berikut:
1. Apakah performa akademik siswa memengaruhi kemungkinan dropout?
2. Apakah faktor finansial seperti status pembayaran dan beasiswa berpengaruh terhadap dropout?
3. Apakah faktor demografi seperti gender dan latar belakang memengaruhi keberhasilan studi?
4. Faktor apa yang paling berpengaruh dalam menentukan siswa akan dropout atau graduate?
5. Seberapa akurat model Machine Learning dalam memprediksi status siswa? 

### Cakupan Proyek
Untuk menjawab permasalahan tersebut, akan dilakukan analisis data dan pengembangan model prediksi menggunakan metode Machine Learning. Proyek ini akan mencakup beberapa pendekatan utama, seperti Exploratory Data Analysis (EDA) untuk memperoleh gambaran terkait dataset yang akan digunakan, pembuatan dashboard, serta pembangunan model klasifikasi untuk memprediksi status siswa. 

Pendekatan Machine Learning yang akan digunakan disesuaikan dengan karakteristik dataset, dengan melakukan perbandingan beberapa algoritma untuk mendapatkan performa terbaik.

Berdasarkan cakupan proyek tersebut, dibutuhkan beberapa resource dan tool, yaitu

- Data performa siswa (Students Performance Dataset)
- Bahasa pemrograman Python sebagai tool utama dalam proyek ini
- Serta, berbagai library pendukung untuk pengolahan data dan pengembangan model machine learning.
- Tools visualisasi seperti Metabase untuk dashboard
- Streamlit untuk deployment model prediksi

### Persiapan

Sumber data:
- [Students' Performance Data](https://github.com/dicodingacademy/dicoding_dataset/blob/bce7a57a496d083716138922bc5839b5c30fa4ea/students_performance/data.csv)

Setup environment:
1. Clone this Repository
   ```bash
   git clone https://github.com/mhddkaa/Institusi-Pendidikan-Problem.git
   ```

2. Install All the Requirements Inside "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Untuk membantu Jaya Jaya institusi dalam memprediksi kemungkinan siswanya dropout dan mencegah hal tersebut lebih dini, dapat menggunakan sistem aplikasi prediksi yang telah dibangun ini. Sistem ini menggunakan Streamlit dan untuk menjalankannya dapat secara local, dengan run code berikut pada Terminal,

```bash
streamlit run app.py
```

Dan untuk menghentikan program aplikasi Streamlit dapat melalui `ctrl + c`.

Sistem prediksi student dropout ini juga dapat diakses secara langsung yang sudah di-deploy ke Streamlit Cloud melalui tautan [berikut ini](https://institusi-pendidikan-problem.streamlit.app/)

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
