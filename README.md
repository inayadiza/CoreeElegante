# Corée Élégante - Korean Fashion Clothing

Ini adalah repository untuk **Corée Élégante**, sebuah aplikasi e-commerce yang dikembangkan untuk **Tugas 2: Pemrograman Berbasis Platform**.

## Deskripsi Proyek
Aplikasi **Corée Élégante** adalah platform e-commerce yang menjual berbagai macam pakaian bergaya Korea yang lucu dan trendi. Pengguna dapat menjelajahi koleksi fashion, melihat detail produk seperti:
- **Nama Produk**
- **Harga**
- **Deskripsi**

# TUGAS 2
## Implementasi demi langkah
Berikut adalah beberapa langkah yang saya lakukan untuk menyelesaikan checklist tugas 2 ini:

1. **Mengonfigurasi Git**
   - Menginstal Git, mengatur nama pengguna dan email, lalu membuat SSH key untuk autentikasi otomatis tanpa password.

2. **Membuat Repositori**
   - Inisiasi repositori lokal dengan `git init`, membuat repositori di GitHub, dan menghubungkannya ke repositori lokal.

3. **Instalasi Virtual Environment**
   - Membuat virtual environment, mengaktifkannya, dan menginstal Django.

4. **Inisiasi Proyek Django**
   - Menjalankan perintah untuk memulai proyek baru, membuat aplikasi, dan mengonfigurasi URL serta pengaturan yang diperlukan.

5. **Mengonfigurasi Arsitektur MVT**
   - Mengonfigurasi URL routing dengan membuat `urls.py` di aplikasi dan menambahkannya ke `urls.py` proyek menggunakan `include()`.
   - Membuat template HTML di direktori `templates` aplikasi.
   - Menggunakan fungsi `render()` di `views.py` untuk menampilkan data dari model.
   - Mendefinisikan model di `models.py`, lalu menjalankan `makemigrations` dan `migrate` untuk menyinkronkan model dengan basis data.

## Bagan Request-Response Django

Berikut adalah bagan dari alur request client ke web aplikasi :
![Flow Diagram](diagram/diagram.jpg)

- **urls.py**: Bertugas untuk menerima request dari client dan memetakan request tersebut ke fungsi yang sesuai di `views.py`. Setiap path di URL ditangani oleh handler tertentu di views.

- **views.py**: Berfungsi untuk mengambil data dari `models.py` (jika diperlukan) dan merender template HTML yang akan dikirimkan kembali kepada client sebagai response. `views.py` mengelola logika di antara URL request, data, dan tampilan.

- **models.py**: Mengelola data yang disimpan dalam database dengan menggunakan Object-Relational Mapping (ORM) yang disediakan oleh Django. Di sini, struktur data dan relasinya didefinisikan dan digunakan oleh `views.py`.

- **templates**: Berisi file HTML yang di-render oleh `views.py` dan ditampilkan kepada pengguna sebagai output. Template ini dapat menggunakan sintaks Django untuk menyisipkan data dinamis dari server ke dalam tampilan statis.

## Fungsi Git dalam Pengembangan Perangkat Lunak
Git berfungsi sebagai sistem kontrol versi yang melacak perubahan kode, memungkinkan kolaborasi, dan mengelola branch untuk pengembangan fitur baru, serta mempermudah pengelolaan proyek perangkat lunak.

## Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?
Menurut saya, framework Django dipilih karena full-stack framework-nya yang lengkap, mudah digunakan, memiliki dokumentasi kuat, dan prinsip "DRY" yang mendorong efisiensi serta kemudahan belajar bagi pemula.

## Mengapa Model pada Django Disebut sebagai ORM?
Model di Django disebut ORM (Object-Relational Mapping) karena memungkinkan pengembang bekerja dengan data sebagai objek Python tanpa menulis SQL secara langsung, sehingga memudahkan interaksi dengan basis data.

# TUGAS 3

### 1. Mengapa pengiriman data penting dalam pengimplementasian sebuah platform?
Pengiriman data sangat penting dalam pengembangan platform karena memungkinkan pertukaran informasi antara klien (front-end) dan server (back-end). Berikut adalah beberapa alasan-alasan pengiriman data menjadi krusial antara lain:
- **Pertukaran Informasi**: Platform memerlukan pengiriman dan penerimaan data secara real-time, seperti pengambilan informasi pengguna atau pengiriman data transaksi. 
- **Sinkronisasi Sistem**: Platform membutuhkan data yang ter-update dari server untuk memberikan informasi yang relevan kepada pengguna.
- **Efisiensi dan Skalabilitas**: Sistem pengiriman data yang baik memastikan efisiensi dalam memproses dan mengelola data secara terstruktur, sehingga mendukung pertumbuhan platform di masa depan.

### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Dibandingkan dengan XML, JSON dianggap lebih unggul dalam hal kecepatan pemrosesan dan kemudahan penggunaan. Salah satu alasan utama mengapa JSON lebih populer adalah karena sintaksnya yang lebih sederhana dan ringan, sehingga mudah dibaca baik oleh manusia maupun mesin. Hal ini berbeda dengan XML yang cenderung lebih verbose dan kompleks. Selain itu, JSON memiliki kinerja yang lebih baik, terutama dalam hal parsing data, karena JSON didukung secara native oleh banyak bahasa pemrograman modern, membuatnya lebih efisien. JSON juga mendapat dukungan luas dalam pengembangan aplikasi web dan API modern, di mana format ini telah menjadi standar utama untuk pertukaran data antara server dan klien. Kombinasi dari kemudahan penggunaan, performa yang lebih cepat, serta dukungan yang luas menjadikan JSON pilihan yang lebih disukai dibandingkan XML dalam banyak aplikasi pengembangan web.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkannya?
Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dimasukkan pengguna ke dalam form. Fungsi ini sangat penting karena:
- **Validasi Data**: Memastikan bahwa data yang dimasukkan sesuai dengan aturan yang telah ditetapkan.
- **Keamanan**: Mencegah input yang tidak valid atau berbahaya dari disimpan di database atau diproses lebih lanjut, sehingga membantu menghindari serangan seperti SQL Injection.
- **Feedback**: Jika data tidak valid, Django akan mengembalikan pesan kesalahan yang dapat ditampilkan kepada pengguna untuk memperbaiki input mereka.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` digunakan di Django untuk mencegah **CSRF (Cross-Site Request Forgery)**, yaitu serangan di mana penyerang dapat memanipulasi pengguna agar mengirimkan permintaan tidak sah kepada aplikasi web tanpa sepengetahuan mereka. Jika form tidak menggunakan `csrf_token`, aplikasi menjadi rentan terhadap:
- **Manipulasi Data**: Penyerang dapat memaksa pengguna yang sudah login untuk mengirimkan form ke server, seperti mengubah data pengguna atau melakukan transaksi tanpa izin.
- **Serangan Keamanan**: Tanpa perlindungan CSRF, data sensitif seperti informasi keuangan atau akun pengguna dapat dieksploitasi.

### 5. Bagaimana cara mengimplementasikan semua langkah-langkah di atas secara step-by-step?
Untuk mengimplementasikan poin-poin di atas, berikut langkah-langkah secara garis besar:

1. **Instalasi Django**: Buat environment virtual dan instal Django menggunakan `pip install django`.
2. **Buat Aplikasi Django**: Inisialisasi proyek Django dengan perintah `django-admin startproject [nama_proyek]`, lalu buat aplikasi dengan `python manage.py startapp [nama_aplikasi]`.
3. **Konfigurasi Pengiriman Data**: Implementasikan API atau views yang dapat menerima dan mengirimkan data dalam format JSON, misalnya menggunakan Django Rest Framework.
4. **Gunakan JSON untuk Pengiriman Data**: Konversi data yang dikirim dari server ke klien menggunakan format JSON.
5. **Penggunaan Forms dengan Validasi**: Buat form Django yang menggunakan method `is_valid()` untuk memvalidasi input dari pengguna.
6. **Implementasi CSRF Protection**: Tambahkan `{% csrf_token %}` di setiap form yang membutuhkan post request untuk melindungi dari serangan CSRF.
7. **Testing dan Debugging**: Uji aplikasi untuk memastikan pengiriman data berjalan dengan baik, validasi form sesuai, dan perlindungan CSRF bekerja.

## Screenshoot Postman
