# closure-shop

### Tautan ke aplikasi pws: http://valentino-vieri-closureshop.pbp.cs.ui.ac.id/

### ===============TUGAS 2===============

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

### ===============TUGAS 3===============

### Repositori ss Postman: https://drive.google.com/drive/folders/1tqC0R31jqp0sihBig_TOYF5xFnWRlhk3?usp=sharing

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

#### Jawab: Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena beberapa alasan. Pertama, data delivery dapat menghemat waktu. Data delivery dapat memastikan pengguna menerima informasi yang dibutuhkan dalam waktu singkat. Kedua, data delivery dapat melakukan sinkronisasi data. Data delivery dapat memastikan data di lebih dari satu komponen dapat tersinkronisasi. Ketiga, data delivery dapat memastikan integritas data. Mekanisme data delivery yang baik dapat memastikan data akan dikirim dengan akurat dan tanpa korupsi selama perjalanan menuju pengguna. Sebenarnya terdapat lebih banyak alasan lainnya terkait kepentingan data delivery dalam pengimplementasian platform, tetapi saya hanya kasih beberapa saja supaya singkat.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

#### Jawab: Menurut saya JSON lebih baik daripada XML karena cara JSON menampilkan data lebih mudah dilihat dan dipahami daripada XML. Berdasarkan Quora, JSON lebih populer dibandingkan XML karena tampilan JSON lebih sederhana daripada XML. Hal ini bisa terjadi karena XML awalnya juga sederhana, tetapi para ahli memutuskan untuk menambahkan berbagai fitur pada XML sehingga XML berubah dari sederhana menjadi sulit. Di sisi lain, JSON awalnya sederhana dan sampai sekarang masih sederhana. Hal ini bisa terjadi karena JSON tidak memiliki semua fitur yang ada pada XML sehingga JSON dapat mempertahankan tampilan sederhana.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

#### Jawab: Fungsi dari method is_valid() pada form Django adalah memvalidasi input. Setiap kali user menekan tombol submit pada form, method is_valid() akan periksa hasil input user dan tampilkan error apabila input tidak sesuai. Method is_valid() dibutuhkan karena beberapa alasan. Pertama, method is_valid() digunakan karena data yang dimasukkan pengguna perlu dipastikan sudah benar. Kedua, method is_valid() digunakan karena method ini bisa memberi error kepada pengguna apabila mereka melakukan kesalahan selama proses input data. Ketiga, method is_valid() digunakan karena kita perlu memastikan input yang dimasukkan pengguna tidak bersifat berbahaya, seperti SQL injection. Dengan method ini, kita dapat memastikan input sudah bersih dan mematuhi format yang diharapkan. Sebenarnya terdapat alasan lainnya terkait kebutuhan method is_valid(), tetapi saya hanya memberi tiga supaya sederhana.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

#### Jawab: Kita membutuhkan csrf_token saat membuat form di Django karena csrf_token dapat mencegah serangan siber yang bernama cross site request forgery (csrf). Kalau kita tidak menambahkan csrf_token, kita bisa saja masuk situs web yang berbahaya dan situs itu meminta kita untuk melakukan hal di situs web lain. Misalnya, kita login dalam situs web bank dan kita pergi ke situs web berbahaya. Situs web berbahaya itu akan mengirim sebuah request untuk transfer uang menggunakan login cookie kita. Situs web bank akan mengira bahwa kita yang membuat request tersebut karena login cookie kita dipakai. Seorang penyerang dapat memanfaatkan aksi ini dengan cara menipu orang, membuat request berbahaya, dan menjalankan perintah.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Jawab:

#### Checklist 1: Pertama, saya buat direktori templates pada direktori root. Kemudian, saya buat base.html pada direktori templates dengan isi berupa template html sehingga saya cukup menggunakan base.html untuk membuat suatu halaman baru. Kemudian saya menambahkan `'DIRS': [BASE_DIR / 'templates'],` pada bagian TEMPLATES di settings.py direktori proyek (closure_shop). Kemudian, saya buat file forms.py pada direktori main. Isi forms.py berupa import ModelForm dan ProductEntry, variabel model untuk menunjukkan saya pakai model ProductEntry, dan fields pada form dengan elemen name, price, dan description. Kemudian, saya import method redirect di views.py main. Kemudian, saya membuat method create_mood_entry dengan parameter request. Kemudian, saya taruh `form = ProductEntryForm(request.POST or None)` untuk membuat ProductEntryForm baru dengan memasukkan QueryDict berdasarkan input user pada request.POST. Kemudian, saya periksa apakah input user valid dan method yang diminta berupa POST. Apabila true, form akan disimpan dan user diarahkan kembali ke halaman main. Kemudian, saya buat dictionary bernama context dengan key form dan value berupa input yang dimasukkan user. Kemudian, saya return render yang akan terima request user, tampilkan create_product_entry.html sebagai halaman form dengan context berupa dictionary. Kemudian, saya update method show_main dengan menampung semua product entry di dalam sebuah variabel dan mengisi context dengan key product_entries dan value berupa isi dari product entry. Kemudian, saya import create_product_entry pada urls.py main dan buat path untuk form product entry. Kemudian, saya buat berkas create_product_entry.html pada direktori templates di main. Dengan berkas ini, saya dapat menampilkan form dalam bentuk tabel dengan csrf_token di atas form untuk mencegah csrf. Terakhir, saya menambahkan kode tambahan di main.html. Inti dari kode tambahan adalah periksa apakah isi product_entries kosong atau tidak. Kalau kosong, kode akan cetak belum ada product. Kalau ada isi, kode akan cetak header tabel dengan isinya berupa hasil input pengguna.

#### Checklist 2: Pertama, saya import HttpResponse dan serializer. Kemudian, saya membuat method show_xml yang menerima request. Di dalam method tersebut, saya simpan semua data object ke dalam variabel data. Selain itu, method tersebut akan mengembalikan sebuah HttpResponse yang mengubah data ke dalam bentuk xml dan content_type berupa application/xml. Kemudian, saya ulangi cara yang sama seperti method show_xml untuk membuat method show_json. Perbedaanya hanya terletak pada penggantian setiap kata xml dengan json. Cara kerjanya juga mirip dengan xml, hanya datanya yang diubah menjadi bentuk json. Kemudian, saya membuat method show_xml_by_id yang menerima request dan sebuah id. Isi method tersebut mirip dengan show_xml. Perbedaannya hanya .all() diubah menjadi .filter(pk=id) yang akan mencari object berdasarkan id unik sebagai primary key dan simpan ke dalam data. Method ini juga mengembalikan hal yang sama seperti method show_xml. Kemudian, saya ulangi cara yang sama seperti method show_xml_by_id untuk method show_json_by_id. Kemudian, saya hanya mengubah semua kata xml dengan json.

#### Checklist 3: Pertama, saya import show_xml, show_json, show_xml_by_id, dan show_json_by_id dari main.views ke dalam file urls.py. Kemudian, saya menambahkan path pada url patterns. Method path() akan menghasilkan isi dari method show_xml, show_json, show_xml_by_id, dan show_json_by_id pada rute masing-masing dengan nama seperti nama method.

#### Checklist 4: Saya hanya menyalin pertanyaan tugas 3 dan menjawab semua pertanyaan satu per satu.

#### Checklist 5: Pertama, saya runserver terlebih dahulu kemudian taruh url http://localhost:8000/xml/ untuk xml, http://localhost:8000/json/ untuk json, http://localhost:8000/xml/[id]/ untuk xml by id, dan http://localhost:8000/json/[id]/ untuk json by id di dalam Postman. Kemudian, saya tekan tombol send dan screenshot hasilnya pada Postman. Saya ulangi langkah ini sampai sudah selesai akses semua empat url. Kemudian, saya taruh gambar di folder pada drive dan set anyone with the link can view. Terakhir, saya taruh pranala folder drive berisi gambar pada README.md.

#### Checklist 6: Pertama, saya menjalankan perintah `git add .` untuk menambahkan semua file yang berubah pada staging. Kedua, saya menjalankan perintah `git commit -m "[Pesan]"` untuk merekam perubahan yang sudah masuk staging di history repositori. Terakhir, saya menjalankan perintah `git push origin main` untuk mendorong perubahan ke branch main repositori closure-shop di GitHub saya.

##### Referensi: chatGPT, tutorial 0, 1, dan 2 PBP, [Quora-Why is JSON so popular](https://www.quora.com/Why-is-JSON-so-popular), [Dokumentasi Django-Forms](https://docs.djangoproject.com/en/5.1/topics/forms/), [Dokumentasi Django-CSRF](https://docs.djangoproject.com/en/5.1/ref/csrf/),
