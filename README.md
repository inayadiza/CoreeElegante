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

# Tugas 4 - Django Authentication, Authorization, dan Manajemen Item

## 1. Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

- **HttpResponseRedirect()**: Kelas respons bawaan Django yang digunakan untuk membuat respons HTTP dengan status 302 (Found). Hal ini berarti sumber daya telah dipindahkan sementara ke URL lain. HttpResponseRedirect() mengharuskan Anda memberikan URL tujuan sebagai argumen secara eksplisit.
- **redirect()**: Fungsi utilitas tingkat tinggi yang juga mengembalikan respons pengalihan (redirect) namun lebih fleksibel. redirect() dapat menerima URL, nama tampilan, atau ID objek, dan secara otomatis menghasilkan URL yang sesuai.

## 2. Cara Kerja Penghubungan Model Product dengan User

Penghubungan antara model Product dan User dilakukan melalui relasi **ForeignKey**. Setiap Product terhubung dengan satu User, yang berarti satu pengguna dapat memiliki banyak Product (relasi one-to-many). Pada model Product, atribut ForeignKey digunakan untuk merujuk ke model User. Jika pengguna dihapus, semua Product yang terkait dengan pengguna tersebut akan dihapus juga secara otomatis karena pengaturan `on_delete=models.CASCADE`, yang memastikan integritas data.

## 3. Perbedaan antara Authentication dan Authorization
### Authentication (Otentikasi)
Otentikasi adalah proses untuk memverifikasi identitas pengguna. Biasanya, ini dilakukan dengan memeriksa username dan password yang dimasukkan oleh pengguna. Contohnya, ketika pengguna memasukkan username dan password dengan benar, mereka akan diizinkan mengakses aplikasi.

### Authorization (Otorisasi)
Otorisasi adalah proses untuk menentukan apakah pengguna yang sudah terotentikasi memiliki izin atau hak akses untuk melakukan tindakan tertentu atau mengakses sumber daya tertentu. Misalnya, meskipun pengguna berhasil login, mereka mungkin tidak diizinkan mengakses halaman admin kecuali memiliki hak akses yang sesuai.

**Apa yang Terjadi Saat Pengguna Login?**
1. **Authentication**: Sistem memeriksa apakah username dan password yang dimasukkan sesuai dengan data di database.
2. **Pembuatan Sesi**: Jika kredensial benar, Django membuat sesi untuk pengguna agar mereka tetap login selama sesi tersebut berlangsung.
3. **Authorization**: Setelah otentikasi, sistem memeriksa izin pengguna untuk menentukan tindakan yang diperbolehkan berdasarkan peran dan izin yang diberikan.

## 4. Implementasi Authentication dan Authorization di Django

### Authentication di Django
Django memiliki sistem otentikasi bawaan untuk memverifikasi identitas pengguna. Beberapa fitur utama meliputi:
- **Model User**: Django menggunakan model `User` dari modul `django.contrib.auth` untuk menyimpan informasi pengguna, seperti username, password, email, dan izin.
- **Fungsi Otentikasi**:
  - `authenticate()`: Memeriksa kredensial pengguna.
  - `login()`: Memulai sesi pengguna yang telah berhasil terotentikasi.
  - `logout()`: Mengakhiri sesi pengguna dan menghapus data sesi.

### Bagaimana Django Mengingat Pengguna yang Telah Login?
Django menggunakan sesi untuk mengingat pengguna yang telah login. Session ID disimpan dalam cookie pada browser pengguna, dan setiap kali pengguna mengunjungi aplikasi, cookie ini dikirimkan ke server sehingga server dapat mengenali pengguna dan menjaga status login mereka.

### Kegunaan Lain dari Cookies
- Menyimpan preferensi pengguna, seperti pengaturan bahasa atau item yang terakhir dilihat.
- Melacak aktivitas pengguna untuk tujuan analitik atau personalisasi.

Namun, tidak semua cookies aman. Cookies dapat disalahgunakan oleh serangan seperti cross-site scripting (XSS). Django menyediakan pengaturan keamanan seperti `HttpOnly`, yang mencegah akses ke cookie oleh JavaScript, serta `Secure`, yang memastikan cookie hanya dikirim melalui koneksi HTTPS.

## 6. Implementasi Checklist
### 1. Membuat Fungsi Registrasi, Login, dan Logout
- Menggunakan `UserCreationForm` untuk registrasi pengguna baru dan `AuthenticationForm` untuk login.
- Setelah login berhasil, sistem membuat session untuk pengguna.
- Saat logout, session dan cookie terkait akan dihapus.

### 2. Membuat Dummy Data untuk Pengguna
- Membuat dua akun pengguna.
- Menambahkan tiga item skincare dummy untuk setiap pengguna, yang dihubungkan melalui model `Item` menggunakan relasi ForeignKey.

### 3. Menghubungkan Model Item dengan User
- Menambahkan atribut `owner` ke model `Item` yang berupa `ForeignKey` ke model `User`. Ini memastikan setiap item dimiliki oleh pengguna yang tepat.

### 4. Menampilkan Username dan Menggunakan Cookie
- Menampilkan username pengguna yang login menggunakan `request.user.username` di halaman utama.
- Mencatat waktu login terakhir menggunakan cookie bernama `last_login`, yang dihapus saat pengguna logout.

### 5. Menyimpan dan Push ke GitHub
- Setelah memastikan fitur berjalan dengan baik, saya melakukan commit terhadap perubahan dan mem-push-nya ke GitHub, sesuai checklist yang ada.