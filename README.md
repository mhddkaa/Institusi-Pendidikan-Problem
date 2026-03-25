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
Student Dropout Problem Dashboard, dirancang untuk menyediakan insight bagi para pihak institusi mengenai tingkat siswa dropout yang mencapai lebih dari 30%. Dashboard ini terdiri dari pie chart tentang summary data siswa, kemudian barchat faktor-faktor dropout mahasiswa.

<img width="1285" height="1332" alt="Putu-Mahdalika-Intan-Pratiwi-dashboard" src="https://github.com/user-attachments/assets/82771956-93fe-49d4-977f-b3956785f47b" />

> **Average of Age** adalah 23.27 tahun, **Average of Admission Grade** adalah 126.98. Menunjukkan mayoritas siswa berada pada usia awal-20an saat masuk dengan nilai akademik yang cukup baik.

> Dari **pie chart status**, terdapat total 4424 siswa, dimana sebanyak 794 (17.95%) yang saat ini sedang terdaftar (enrolled), 2209 (49.93%) yang sudah lulus (graduate), dan 1421 (32.12%) yang *dropout*. Hal ini menunjukkan bahwa tingkat *dropout* masih tergolong tinggi, hampir 1/3 dari total siswa.

> Dari **pie chart debitur** sebanyak 11.37% adalah seorang debitur, dan 88.63% sisanya tidak.

> Dari **pie chart gender**, dapat diketahui bahwa didominasi oleh jenis kelamin perempuan, sebesar 2868 (64.83%), sedangkan laki-laki sebanyak 1556 (35.17%).
   
> Dari **pie chart beasiswa**, sebesar  1099 (24.84%) siswa yang memperoleh beasiswa, sedangkan 3325 (75.16%) sisanya tidak.  

> Dari **bar chart status siswa berdasarkan status debtor**, terlihat bahwa siswa yang menjadi debitur paling banyak berada pada status dropout (312 siswa) dibandingkan yang lulus (101 siswa). Hal ini menunjukkan bahwa faktor finansial memiliki pengaruh kuat terhadap kemungkinan mahasiswa mengalami dropout.

> Dari **bar chart status siswa berdasarkan beasiswa**, terdapat 835 siswa lulus dengan beasiswa dan 1,374 lulus tanpa beasiswa (37.79% vs 62.20%). Sementara itu, siswa yang dropout dengan beasiswa hanya 134, dibandingkan 1,287 tanpa beasiswa (9.43% vs 90.57%). Ini menunjukkan bahwa beasiswa berperan signifikan dalam menurunkan risiko dropout.

> Dari **bar chart performa semester 1 & 2**, siswa yang lulus memiliki nilai yang lebih tinggi dan cenderung meningkat di semester 2, sedangkan siswa dropout memiliki nilai lebih rendah sejak semester awal. Hal ini menunjukkan bahwa performa akademik di awal studi menjadi indikator penting terhadap keberhasilan kelulusan.

> Dari **bar chart top courses** dengan dropout tertinggi, jurusan seperti Management, Nursing, dan Journalism and Communication memiliki jumlah dropout paling tinggi dibandingkan jurusan lainnya.

> Dari **histogram usia siswa**, terlihat bahwa mayoritas siswa berada pada rentang usia 18–25 tahun, dengan jumlah semakin menurun pada usia yang lebih tinggi. Ini menunjukkan bahwa populasi siswa didominasi oleh usia muda dan relatif homogen.

> Dari **chart status berdasarkan marital status**, mayoritas siswa berstatus single, baik yang lulus, dropout, maupun masih terdaftar. Status menikah dan lainnya memiliki jumlah yang jauh lebih kecil, sehingga tidak terlalu dominan dalam memengaruhi distribusi status siswa.

1. Mengakses Dashboard Analisis Metabase
   ```bahs
   Login Metabase
       Username: mahdaalikap@gmail.com
       Password: root123 
   ```

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
