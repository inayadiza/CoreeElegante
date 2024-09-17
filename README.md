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

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery itu penting banget dalam platform karena memungkinkan kita mengirimkan data dari satu bagian sistem ke bagian lainnya, misalnya dari client ke server. Dengan ini memungkinkan aplikasi kita untuk dinamis dan interaktif, di mana data bisa dikirim, disimpan, dan diambil sesuai kebutuhan.

### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih sering digunakan daripada XML karena lebih ringan dan lebih mudah dibaca. Sintaks JSON lebih sederhana dan tidak bertele-tele seperti XML yang memerlukan banyak tag pembuka dan penutup. Oleh karena itu, JSON lebih cepat dan lebih efisien, terutama dalam aplikasi web modern.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` berfungsi untuk memvalidasi input dari form sebelum data disimpan. Kita butuh method ini untuk memastikan bahwa data yang diinput oleh pengguna sesuai dengan aturan yang sudah ditentukan di model. Kalau tidak valid, Django akan mengembalikan error, sehingga kita bisa menangani kesalahan sebelum data disimpan.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` sangat penting untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Tanpa `csrf_token`, form kita rentan terhadap serangan di mana penyerang bisa membuat request yang tidak sah dari luar aplikasi. Jika tidak ditambahkan, aplikasi bisa dieksploitasi dengan mengirimkan request berbahaya seolah-olah berasal dari pengguna sah.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?

1. **Membangun Kerangka Views (Skeleton):**
   - Pertama, membuat folder `templates` dan file `base.html`
   File ini berfungsi sebagai kerangka dasar yang akan di-extend oleh halaman lain. Dengan menggunakan kerangka ini, desain web bisa lebih konsisten dan kode jadi lebih rapi.
   - Dalam `base.html`, menambahkan tag `{% block %}` untuk membuat area yang nanti bisa diisi atau diubah oleh halaman lain.

2. **Mengganti Primary Key dari Integer ke UUID:**
   - Impor `uuid` di `models.py` dan mengganti field `id` di model `MoodEntry` dengan `UUIDField`. 
   Hal ini supaya setiap data mood punya ID unik yang lebih aman dan tidak bisa ditebak seperti ID integer.

3. **Membuat Form untuk Input Data Mood:**
   - Membuat file `forms.py` yang mendefinisikan form untuk input data
   - Kemudian, di `views.py`, membuat fungsi `create_clothing_entry` untuk menampilkan form dan menyimpan data yang di-submit oleh user ke database serta menambahkan `{% csrf_token %}` di template HTML untuk mengamankan form dari serangan.

4. **Mengembalikan Data dalam Format XML dan JSON:**
   - Di sini membuat dua fungsi, `show_xml` dan `show_json`, di `views.py`. 
   Keduanya bertanggung jawab untuk mengubah data ke format XML atau JSON. Setelah itu, menambahkan URL routing di `urls.py` supaya bisa diakses di browser atau API.

5. **Testing dengan Postman:**
   - Setelah server Django berjalan, membuka Postman dan coba kirim request GET ke endpoint `xml/` atau `json/` untuk melihat apakah data muncul dengan format yang benar. 
   Hal ini membantu memvalidasi bahwa data sudah dikirim dan diterima dengan baik oleh API.

## Screenshoot Postman
![Postman JSON](screenshoot/Screenshot%202024-09-17%20224213.png)
![Postman JSON ID](screenshoot/Screenshot%202024-09-17%20224755.png)
![Postman XML](screenshoot/Screenshot%202024-09-17%20224148.png)
![Postman XML ID](screenshoot/Screenshot%202024-09-17%20224721.png)