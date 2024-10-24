# 99_data_engrg_test

Deskripsi Proyek

Repositori ini berisi dua tugas:

Analisis Ketergantungan File SQL (master.py): Sebuah skrip Python yang membaca file SQL dari direktori dan menganalisis ketergantungan antar file.
Analisis Data Properti (main.ipynb): Sebuah Jupyter Notebook yang melakukan analisis statistik pada data properti menggunakan Pandas.
1. Analisis Ketergantungan File SQL (master.py)
Skrip ini melakukan langkah-langkah berikut:

Membaca File SQL: Memindai direktori yang diberikan untuk file SQL, membaca isinya, dan menyimpannya dalam dictionary dengan nama file sebagai kunci.
Menemukan Ketergantungan: Memeriksa referensi ke file SQL lain dalam konten tiap file untuk menentukan ketergantungan antar file.
Topological Sorting: Melakukan pengurutan topologis terhadap file SQL berdasarkan ketergantungannya, sehingga file diolah dalam urutan yang benar.
Cara Penggunaan:

Letakkan file SQL Anda dalam direktori tertentu.
Jalankan skrip dengan menentukan jalur direktori.
Skrip akan menampilkan ketergantungan file SQL dan urutan eksekusinya.
Fungsi Utama:

read_sql_files(directory): Membaca semua file SQL dalam direktori dan mengembalikan dictionary berisi konten file.
find_dependencies(sql_files): Menganalisis ketergantungan antara file SQL.
topological_sort(dependencies): Mengurutkan file SQL berdasarkan ketergantungan.
2. Analisis Data Properti (main.ipynb)
Jupyter Notebook ini menganalisis dataset yang berisi informasi tentang berbagai properti. Notebook ini menggunakan Pandas untuk menghitung statistik deskriptif pada kolom seperti price, bedRooms, bathRooms, landSize, dan buildingSize.

Langkah Utama:

Memuat Data: Dataset dimuat ke dalam DataFrame Pandas.
Statistik Deskriptif: Notebook menghitung statistik ringkasan (mean, std, min, max, dll.) untuk berbagai atribut properti.
Visualisasi: Langkah-langkah selanjutnya bisa melibatkan visualisasi data untuk mendapatkan wawasan lebih dalam.
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
