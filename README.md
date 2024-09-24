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

# TUGAS 4
### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
- HttpResponseRedirect() adalah kelas respons langsung dari Django yang digunakan untuk membuat respons HTTP dengan status 302 (Found), yang berarti sumber daya telah dipindahkan sementara ke URL lain. Penggunaannya jauh lebih eksplisit, dan harus memberikan URL tujuan sebagai argumen.
- redirect() adalah fungsi utilitas yang lebih tinggi tingkatannya yang juga mengembalikan respons pengalihan, tetapi dengan tambahan kemudahan dan fleksibilitas. Fungsi redirect() ini dapat menerima URL langsung, nama tampilan, atau ID objek, dan secara otomatis akan membangun URL yang sesuai.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan User dilakukan melalui relasi ForeignKey, di mana setiap Product terhubung dengan satu User yang berarti satu pengguna dapat memiliki banyak Product, yang dikenal sebagai relasi one-to-many. Pada model Product, atribut ForeignKey digunakan untuk merujuk ke model User. Pengaturan ini memungkinkan setiap Product terkait langsung dengan satu pengguna. Jika pengguna dihapus, semua Product yang dimilikinya juga akan dihapus secara otomatis karena pengaturan on_delete=models.CASCADE, yang memastikan integritas data tetap terjaga.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

## Perbedaan antara Authentication dan Authorization
### 1. Authentication
Authentication adalah proses memverifikasi identitas pengguna untuk memastikan bahwa pengguna adalah orang yang mereka klaim. Ini biasanya dilakukan dengan memasukkan username dan password. Contohnya, ketika pengguna memasukkan username dan password untuk masuk ke dalam aplikasi. Hasilnya, jika username dan password benar, pengguna dianggap terotentikasi dan diizinkan mengakses aplikasi.

### 2. Authorization (Otorisasi)
Authorization adalah proses menentukan apakah pengguna yang telah terotentikasi memiliki izin atau hak akses untuk melakukan tindakan tertentu atau mengakses sumber daya tertentu. Contohnya, setelah login, seorang pengguna mungkin bisa melihat beberapa halaman, tetapi tidak dapat mengakses halaman admin atau mengubah data kecuali memiliki hak akses yang tepat. Authorization menentukan apa saja yang dapat dilakukan oleh pengguna yang telah terotentikasi di dalam aplikasi, berdasarkan peran dan izin mereka.

## Apa yang Terjadi Saat Pengguna Login?
Ketika pengguna login, beberapa langkah terjadi:
1. **Proses Authentication**: Sistem memeriksa apakah username dan password yang dimasukkan cocok dengan data yang ada di database.
2. **Pembuatan Sesi**: Jika kredensial benar, Django membuat sesi untuk pengguna sehingga mereka tetap login selama sesi berlangsung.
3. **Proses Authorization**: Setelah pengguna terotentikasi, sistem akan memeriksa hak akses pengguna untuk memastikan mereka hanya bisa melakukan tindakan sesuai dengan izin yang diberikan.

## Implementasi Authentication dan Authorization di Django
### Authentication di Django
Django memiliki sistem otentikasi bawaan yang memungkinkan verifikasi identitas pengguna. Beberapa fitur utama:
- **Model User**: Django menggunakan model `User` yang disediakan oleh modul `django.contrib.auth` untuk mengelola data pengguna seperti username, password, email, dan izin.
- **Fungsi Authentication**:
  - `authenticate()`: Memeriksa kredensial pengguna.
  - `login()`: Memulai sesi untuk pengguna yang berhasil terotentikasi.
  - `logout()`: Mengakhiri sesi pengguna yang login.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan memanfaatkan session, yang diidentifikasi oleh session ID yang disimpan di cookie pada browser pengguna. Setiap kali pengguna mengunjungi aplikasi, browser akan mengirimkan cookie yang berisi session ID tersebut ke server. Berdasarkan session ID ini, server dapat mengenali pengguna dan menjaga status login mereka.

**Cookies juga memiliki kegunaan lain, seperti**:
- Menyimpan preferensi pengguna, seperti pengaturan bahasa atau item yang baru saja dilihat.
- Melacak aktivitas pengguna di situs web, misalnya untuk tujuan analitik atau personalisasi.

Namun, tidak semua cookies aman. Cookies dapat menjadi sasaran serangan seperti cross-site scripting (XSS). Django memiliki pengaturan keamanan seperti `HttpOnly`, yang mencegah cookie diakses oleh JavaScript, serta `Secure`, yang memastikan cookie hanya dikirimkan melalui koneksi HTTPS, untuk meningkatkan keamanan penggunaan cookies.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**1. Membuat Fungsi Registrasi, Login, dan Logout**: Saya menggunakan `UserCreationForm` untuk proses registrasi pengguna baru, dan `AuthenticationForm` untuk proses login. Setelah pengguna berhasil login, sistem membuat session yang terkait dengan pengguna tersebut. Saat pengguna logout, session beserta cookie yang terkait akan dihapus.
**2. Membuat Dummy Data untuk Pengguna**: Saya membuat dua akun pengguna dan menambahkan tiga item skincare dummy untuk setiap pengguna. Setiap item dihubungkan dengan pengguna melalui model `Item`, menggunakan relasi ForeignKey.
**3.Menghubungkan Model Item dengan User**: Di model `Item`, saya menambahkan atribut `owner` yang merupakan relasi ForeignKey ke model `User`, untuk memastikan setiap item skincare dimiliki oleh pengguna tertentu.
**4.Menampilkan Username dan Menggunakan Cookie**: Saya menampilkan username pengguna yang sedang login di halaman utama menggunakan `request.user.username`. Saya juga mencatat waktu login terakhir pengguna menggunakan cookie bernama `last_login`, yang akan dihapus saat pengguna melakukan logout.
**5.Menyimpan dan Push ke GitHub**: Setelah memastikan semua fitur berfungsi dengan baik, saya melakukan commit terhadap perubahan dan mem-push-nya ke GitHub, sesuai dengan checklist yang ada.