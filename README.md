## Implementasi demi langkah
Berikut adalah beberapa langkah yang saya lakukan untuk menyelesaikan checklist tugas 2 ini :
** 1. Mendaftar di GitHub
Membuat akun, memverifikasi email, dan menyesuaikan profil untuk proyek dan kolaborasi.

** 2. Mengonfigurasi Git
- Menginstal Git, mengatur nama pengguna dan email dengan git config, lalu membuat SSH key untuk autentikasi otomatis tanpa password.

** 3. Membuat Repositori
- Inisiasi repositori lokal dengan git init, membuat repositori di GitHub, dan menghubungkannya dengan git remote add origin <URL_REPO>.

** 4. Instalasi Virtual Environment
- Membuat virtual environment dengan python -m venv env, mengaktifkannya, dan menginstal Django menggunakan pip install django.

** 5. Inisiasi Proyek Django
- Menjalankan django-admin startproject <project_name>, membuat aplikasi dengan startapp, dan mengonfigurasi URL serta settings yang diperlukan.
Mengonfigurasi Arsitektur MVT

**6. Mengonfigurasi URL routing dengan membuat urls.py di aplikasi dan menambahkannya ke urls.py proyek menggunakan include().
- Membuat template HTML di direktori templates aplikasi.
- Menggunakan fungsi render() di view untuk menampilkan data dari model.
- Mendefinisikan model di models.py, lalu menjalankan makemigrations dan migrate untuk menyinkronkan model dengan basis data.


## Bagan Request-Response Django

Berikut adalah bagan dari alur request cilent ke web aplikasi 
![Django Flow Diagram](images/diagram.jpg)
- urls.py: Bertugas untuk menerima request dari client dan memetakan request tersebut ke fungsi yang sesuai di views.py. Setiap path di URL ditangani oleh handler tertentu di views.

- views.py: Berfungsi untuk mengambil data dari models.py (jika diperlukan) dan merender template HTML yang akan dikirimkan kembali kepada client sebagai response. views.py mengelola logika di antara URL request, data, dan tampilan.

- models.py: Mengelola data yang disimpan dalam database dengan menggunakan Object-Relational Mapping (ORM) yang disediakan oleh Django. Di sini, struktur data dan relasinya didefinisikan dan digunakan oleh views.py.

- templates: Berisi file HTML yang di-render oleh views.py dan ditampilkan kepada pengguna sebagai output. Template ini dapat menggunakan sintaks Django untuk menyisipkan data dinamis dari server ke dalam tampilan statis.

## Fungsi git dalam pengembangan perangkat lunak
Git berfungsi sebagai sistem kontrol versi yang melacak perubahan kode, memungkinkan kolaborasi, dan mengelola branch untuk pengembangan fitur baru, serta mempermudah pengelolaan proyek perangkat lunak.

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dipilih karena full-stack framework-nya yang lengkap, mudah digunakan, memiliki dokumentasi kuat, dan prinsip "DRY" yang mendorong efisiensi serta kemudahan belajar bagi pemula.

## Mengapa model pada Django disebut sebagai ORM?
Model di Django disebut ORM (Object-Relational Mapping) karena memungkinkan pengembang bekerja dengan data sebagai objek Python tanpa menulis SQL secara langsung, sehingga memudahkan interaksi dengan basis data.