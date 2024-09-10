# closure-shop

### Tautan ke aplikasi pws: http://valentino-vieri-closureshop.pbp.cs.ui.ac.id/

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Jawab:

#### Checklist 1: Pertama, saya buat repositori closure-shop di GitHub, kemudian clone menjadi repositori lokal. Kemudian, saya setup virtual environment dan aktivasinya. Setelah itu, saya membuat requirements.txt dan mengunduh semua dependencies yang ada di dalamnya. Kemudian, saya membuat project closure_shop dengan bantuan django admin. Setelah itu, saya menambahkan localhost dan 127.0.0.1 ke dalam ALLOWED_HOSTS. Kemudian, saya runserver dengan bantuan manage.py dan deactivate environment. Terakhir, saya menambahkan berkas .gitignore ke dalam direktori utama (closure-shop), git add, git commit -m, dan git push ke repositori closure-shop di GitHub.

#### Checklist 2: Saya membuat aplikasi main dengan bantuan manage.py dan menambahkan main ke dalam INSTALLED_APPS pada berkas settings.py dalam direktori proyek (mental_health_tracker).

#### Checklist 3: Pertama, saya mengimpor fungsi include dari django.urls. Kemudian, saya menambahkan path ke halaman utama yang memiliki rute ke module main.urls.

#### Checklist 4: Pertama, saya lihat tutorial 1 sebagai referensi. Kemudian, saya import models dari django.db. Kemudian, saya membuat model Product dengan atribut name, price, dan description. Atribut ini tidak bersifat mutlak karena ada saya mungkin menambahkan atribut lainnya pada tugas berikutnya. Oleh karena itu, saya kasih atribut dasar dulu. Kemudian, saya makemigrations dan migrate dengan bantuan manage.py. Perintah makemigrations akan membuat berkas basis data dan perintah migrate akan menerapkan migrasi ke basis data lokal.

#### Checklist 5: Pertama, saya membuat fungsi show_main yang menerima parameter request supaya bisa terima request pengguna. Kemudian, saya membuat context yang berisi nama aplikasi, nama, dan kelas saya. Kemudian, saya kembalikan hasil fungsi render yang menerima parameter request, berkas html, dan isinya (context). Terakhir, saya ubah main.html supaya bisa menampilkan isi dari context.

#### Checklist 6: Pertama, saya impor path dari django.urls dan fungsi show_main dari modul main.views sebagai tampilan halaman. Kemudian, saya namakan app_name sebagai main sehingga menjadi nama unik pada pola url. Terakhir, saya menggunakan fungsi path dalam urlpatterns pergi ke route halaman utama dengan view berupa pemanggilan fungsi show_main dan name berupa show_main.

#### Checklist 7: Pertama, saya buka halaman PWS dan login. Kemudian, saya create project dengan nama closureshop dan simpan credentials. Kemudian saya menambahkan URL deployment pws di ALLOWED_HOSTS yang berada di settings.py. Kemudian, saya jalankan perintah yang ada di pws supaya situs web diakses di internet. Kemudian, saya ganti nama branch utama menjadi main. Terakhir, saya tekan view projects untuk melihat situs web setelah statusnya running di pws.

#### Checklist 8: Saya hanya menyalin tautan ke aplikasi pws dan jawab pertanyaan.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

#### Jawab:

#### Pranala bagan: https://drive.google.com/file/d/1Ia9LBK7WopK-_VSgR7DWo4vfZtYm176J/view?usp=sharing

#### Dalam request client ke web aplikasi berbasis Django, terdapat urls.py, views.py, models.py, dan berkas html. Berkas models.py terdapat pada bagian models karena berkas tersebut mengatur data suatu web aplikasi. Berkas html terdapat pada bagian template karena berkas tersebut mengatur tampilan utama web aplikasi. Berkas views.py terletak di bagian views karena berkas ini mengatur pengambilan data serta berkas html untuk menampilkan suatu halaman web aplikasi ke pengguna. Berkas urls.py tidak terikat pada satu bagian tertentu karena berkas ini mengatur rute yang harus diikuti pengguna apabila mereka ingin menuju halaman tertentu. Secara keseluruhan, urls.py mengatur rute supaya pengguna bisa pergi ke halaman yang ditampilkan views.py setelah mengambil data dari models.py dan berkas html.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

#### Jawab:

#### a. Git berfungsi sebagai sistem kontrol versi perangkat lunak dengan cara memantau versi-versi suatu perangkat lunak. Hal ini bisa membantu para pengembang perangkat lunak (software developer) untuk uji coba suatu kode. Apabila kode berhasil, versi baru bisa disebarkan. Apabila gagal, mereka bisa kembali ke versi sebleumnya saja.

#### b. Git juga berfungsi sebagai tempat kolaborasi dengan orang lain. Dengan Git, orang yang memiliki akses ke repositori tertentu bisa kerja sama untuk mengembangkan suatu perangkat lunak. Dengan lebih banyak orang yang kerja sama, suatu proyek perangkat lunak dapat dikembangkan dengan kecepatan yang lebih tinggi daripada seseorang buat sendiri.

#### c. Git juga berfungsi sebagai tempat staging. Dengan fungsi ini, seorang pengembang perangkat lunak mampu memilih perubahan apa saja yang perlu di commit ddan perubahan apa saja yang tidak perlu di commit dulu.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

#### Jawab: Menurut saya, Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django lumayan sederhana dan tidak terlalu rumit. Framework yang memiliki sifat ini cocok bagi pemula yang tidak memiliki pengalaman dalam menggunakan framework perangkat lunak. Bahkan, saya sendiri (yang tidak memiliki pengalaman pakai framework Django) merasa lumayan percaya diri saat menggunakan Django untuk membuat situs web. Hal ini bisa terjadi karena sifat Django yang sederhana dan tidak terlalu rumit sehingga situs web dapat dikembangkan dalam waktu singkat.

### 5. Mengapa model pada Django disebut sebagai ORM?

#### Jawab: Model Django disebut sebagai ORM (Object-Relational Mapping) karena Django memiliki unsur relational model dan object-oriented data model. Unsur object-oriented data model bisa dilihat dengan jelas pada tugas ini karena dalam main.model terdapat class dengan atribut tertentu. Apabila ada class, berarti ada juga object. Unsur relational model juga ada di Django karena ada field OneToOneField, ForeignKey, ManyToManyField, dll yang merupakan bagian relational model. Namun, unsur relationship belum terlihat karena dua alasan spekulasi. Pertama, mata kuliah basis data belum diambil oleh semua mahasiswa semester 3 sehingga tidak ditaruh di PBP. Kedua, unsur relationship mungkin terlihat di tutorial berikutnya sehingga saya belum melihat implementasinya.

##### Referensi: chatGPT, tutorial 0 dan 1 PBP,
