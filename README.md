# closure-shop

### Tautan ke aplikasi pws:

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Jawab:

#### Checklist 1: Pertama, saya buat repositori closure-shop di GitHub, kemudian clone menjadi repositori lokal. Kemudian, saya setup virtual environment dan aktivasinya. Setelah itu, saya membuat requirements.txt dan mengunduh semua dependencies yang ada di dalamnya. Kemudian, saya membuat project closure_shop dengan bantuan django admin. Setelah itu, saya menambahkan localhost dan 127.0.0.1 ke dalam ALLOWED_HOSTS. Kemudian, saya runserver dengan bantuan manage.py dan deactivate environment. Terakhir, saya menambahkan berkas .gitignore ke dalam direktori utama (closure-shop), git add, git commit -m, dan git push ke repositori closure-shop di GitHub.

#### Checklist 2: Saya membuat aplikasi main dengan bantuan manage.py dan menambahkan main ke dalam INSTALLED_APPS pada berkas settings.py dalam direktori proyek (mental_health_tracker).

#### Checklist 3:

#### Checklist 4: Pertama, saya lihat tutorial 1 sebagai referensi. Kemudian, saya import models dari django.db. Kemudian, saya membuat model Product dengan atribut name, price, description, dan stock. Atribut ini tidak bersifat mutlak karena ada saya mungkin menambahkan atribut lainnya pada tugas berikutnya. Oleh karena itu, saya kasih atribut dasar dulu. Kemudian, saya makemigrations dan migrate dengan bantuan manage.py. Perintah makemigrations akan membuat berkas basis data dan perintah migrate akan menerapkan migrasi ke basis data lokal.

#### Checklist 5: Pertama, saya membuat fungsi show_main yang menerima parameter request supaya bisa terima request pengguna. Kemudian, saya membuat context yang berisi nama dan kelas saya. Kemudian, saya kembalikan hasil fungsi render yang menerima parameter request, berkas html, dan isinya (context). Terakhir, saya ubah main.html supaya bisa menampilkan isi dari context.

#### Checklist 6:

#### Checklist 7:

#### Checklist 8: Saya hanya menyalin tautan ke aplikasi pws dan jawab pertanyaan.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

#### Jawab: Menurut saya, Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django lumayan sederhana dan tidak terlalu rumit. Framework yang memiliki sifat ini cocok bagi pemula yang tidak memiliki pengalaman dalam menggunakan framework perangkat lunak. Bahkan, saya sendiri (yang tidak memiliki pengalaman pakai framework Django) merasa lumayan percaya diri saat menggunakan Django untuk membuat situs web. Hal ini bisa terjadi karena sifat Django yang sederhana dan tidak terlalu rumit sehingga situs web dapat dikembangkan dalam waktu singkat.

### 5. Mengapa model pada Django disebut sebagai ORM?
