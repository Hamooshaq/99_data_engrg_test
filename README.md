# 99_data_engrg_test

## Deskripsi Test

### Repositori ini berisi dua test:

1. Analisis Ketergantungan File SQL (data_engrg_test1/master.py): Code Python yang membaca file SQL dari direktori dan menganalisis dependencies antar file.
2. Analisis Data Properti (data_engrg_test2/data-interview-99-main.ipynb): Code python(ipynb) untuk melakukan analisis statistik pada data properti menggunakan Pandas.
   
#### 1. Analisis Ketergantungan File SQL (master.py)
Code ini melakukan langkah-langkah berikut:

Membaca File SQL: Membaca direktori yang diberikan untuk file SQL, membaca isinya, dan menyimpannya dalam dictionary dengan nama file sebagai kunci.
Menemukan Ketergantungan: Memeriksa referensi ke file SQL lain dalam konten tiap file untuk menentukan dependencies antar file.
Topological Sorting: Melakukan pengurutan topologi terhadap file SQL berdasarkan dependencies, sehingga file diolah dalam urutan yang benar.
Cara Penggunaan:

Letakkan file SQL dalam direktori.
Jalankan code dengan menentukan jalur direktori.
code akan mengeluarkan output dependencies file SQL dan urutan eksekusinya.
Fungsi Utama:

read_sql_files(directory): Membaca semua file SQL dalam direktori dan mengembalikan dictionary berisi konten file.
find_dependencies(sql_files): Menganalisis dependencies antara file SQL.
topological_sort(dependencies): Mengurutkan file SQL berdasarkan dependencies.

#### 2. Analisis Data Properti (main.ipynb)
Code ini menganalisis dataset yang berisi informasi tentang berbagai properti. Code ini menggunakan Pandas untuk menghitung statistik pada kolom seperti price, bedRooms, bathRooms, landSize, dan buildingSize.

Langkah Utama:

Load Data: Dataset dibaca ke dalam DataFrame Pandas.
Statistik: Code menghitung statistik ringkasan (mean, std, min, max, dll.) untuk berbagai atribut properti.
Visualisasi: Langkah-langkah selanjutnya melibatkan visualisasi data untuk mendapatkan informasi lebih dalam.
Ketergantungan:

Python 3.x
Pandas
Jupyter Notebook
Cara Menjalankan
Untuk skrip Python (master.py):
Pastikan Python 3.x terinstal.
Jalankan skrip menggunakan:
bash
Copy code
python master.py
Tentukan direktori yang berisi file SQL Anda.
Untuk Jupyter Notebook (main.ipynb):
Buka notebook di JupyterLab atau Jupyter Notebook.
Jalankan semua sel untuk melakukan analisis data.



Link Google Slide untuk Test 2:
https://docs.google.com/presentation/d/1yJh1wgiRH0JMwTUBPMcFZKHyuoNMWh2nz7qZTdrE4e8/edit?usp=sharing

