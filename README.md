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

#### Checklist 1: Pertama, saya buat direktori templates pada direktori root. Kemudian, saya buat base.html pada direktori templates dengan isi berupa template html sehingga saya cukup menggunakan base.html untuk membuat suatu halaman baru. Kemudian saya menambahkan `'DIRS': [BASE_DIR / 'templates'],` pada bagian TEMPLATES di settings.py direktori proyek (closure_shop). Kemudian, saya buat file forms.py pada direktori main. Isi forms.py berupa import ModelForm dan ProductEntry, variabel model untuk menunjukkan saya pakai model ProductEntry, dan fields pada form dengan elemen name, price, dan description. Kemudian, saya import method redirect di views.py main. Kemudian, saya membuat method create_product_entry dengan parameter request. Kemudian, saya taruh `form = ProductEntryForm(request.POST or None)` untuk membuat ProductEntryForm baru dengan memasukkan QueryDict berdasarkan input user pada request.POST. Kemudian, saya periksa apakah input user valid dan method yang diminta berupa POST. Apabila true, form akan disimpan dan user diarahkan kembali ke halaman main. Kemudian, saya buat dictionary bernama context dengan key form dan value berupa input yang dimasukkan user. Kemudian, saya return render yang akan terima request user, tampilkan create_product_entry.html sebagai halaman form dengan context berupa dictionary. Kemudian, saya update method show_main dengan menampung semua product entry di dalam sebuah variabel dan mengisi context dengan key product_entries dan value berupa isi dari product entry. Kemudian, saya import create_product_entry pada urls.py main dan buat path untuk form product entry. Kemudian, saya buat berkas create_product_entry.html pada direktori templates di main. Dengan berkas ini, saya dapat menampilkan form dalam bentuk tabel dengan csrf_token di atas form untuk mencegah csrf. Terakhir, saya menambahkan kode tambahan di main.html. Inti dari kode tambahan adalah periksa apakah isi product_entries kosong atau tidak. Kalau kosong, kode akan cetak belum ada product. Kalau ada isi, kode akan cetak header tabel dengan isinya berupa hasil input pengguna.

#### Checklist 2: Pertama, saya import HttpResponse dan serializer. Kemudian, saya membuat method show_xml yang menerima request. Di dalam method tersebut, saya simpan semua data object ke dalam variabel data. Selain itu, method tersebut akan mengembalikan sebuah HttpResponse yang mengubah data ke dalam bentuk xml dan content_type berupa application/xml. Kemudian, saya ulangi cara yang sama seperti method show_xml untuk membuat method show_json. Perbedaanya hanya terletak pada penggantian setiap kata xml dengan json. Cara kerjanya juga mirip dengan xml, hanya datanya yang diubah menjadi bentuk json. Kemudian, saya membuat method show_xml_by_id yang menerima request dan sebuah id. Isi method tersebut mirip dengan show_xml. Perbedaannya hanya .all() diubah menjadi .filter(pk=id) yang akan mencari object berdasarkan id unik sebagai primary key dan simpan ke dalam data. Method ini juga mengembalikan hal yang sama seperti method show_xml. Kemudian, saya ulangi cara yang sama seperti method show_xml_by_id untuk method show_json_by_id. Kemudian, saya hanya mengubah semua kata xml dengan json.

#### Checklist 3: Pertama, saya import show_xml, show_json, show_xml_by_id, dan show_json_by_id dari main.views ke dalam file urls.py. Kemudian, saya menambahkan path pada url patterns. Method path() akan menghasilkan isi dari method show_xml, show_json, show_xml_by_id, dan show_json_by_id pada rute masing-masing dengan nama seperti nama method.

#### Checklist 4: Saya hanya menyalin pertanyaan tugas 3 dan menjawab semua pertanyaan satu per satu.

#### Checklist 5: Pertama, saya runserver terlebih dahulu kemudian taruh url http://localhost:8000/xml/ untuk xml, http://localhost:8000/json/ untuk json, http://localhost:8000/xml/[id]/ untuk xml by id, dan http://localhost:8000/json/[id]/ untuk json by id di dalam Postman. Kemudian, saya tekan tombol send dan screenshot hasilnya pada Postman. Saya ulangi langkah ini sampai sudah selesai akses semua empat url. Kemudian, saya taruh gambar di folder pada drive dan set anyone with the link can view. Terakhir, saya taruh pranala folder drive berisi gambar pada README.md.

#### Checklist 6: Pertama, saya menjalankan perintah `git add .` untuk menambahkan semua file yang berubah pada staging. Kedua, saya menjalankan perintah `git commit -m "[Pesan]"` untuk merekam perubahan yang sudah masuk staging di history repositori. Terakhir, saya menjalankan perintah `git push origin main` untuk mendorong perubahan ke branch main repositori closure-shop di GitHub saya.

### ===============TUGAS 4===============

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

#### Jawab: HttpResponseRedirect() adalah sebuah fungsi yang menerima sebuah url dan mengarahkan user ke url yang dituliskan sebagai argumen di dalamnya. Fungsi redirect() bekerja dengan cara yang mirip dengan HttpResponseRedirect(), tetapi redirect() bisa berisi argumen berupa url atau sebuah nama di view sehingga sifatnya lebih fleksibel dan mudah. Jadi, HttpResponseRedirect() adalah cara yang cepat untuk mengarahkan user ke url tertentu, sedangkan redirect() adalah cara yang mudah untuk mengarahkan user ke url tertentu tanpa harus mengisi argumen berupa url asli ke halaman tertentu.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!

#### Jawab: Model Product dihubungkan dengan User melalui Foreign Key ke entity User. Foreign key adalah sebuah atribut dari Product yang dihubungkan ke primary key dari User sehingga terbentuk suatu relasi. Foreign key ini harus bersifat unik sehingga tidak mungkin ada produk yang sama dipetakan ke user berbeda. Selain itu, primary key user juga dijamin unik sehingga peluang dua user dapat saling lihat product mereka menjadi kecil, bahkan bisa mendekati 0. Dengan cara inilah, model Product dapat dihubungkan dengan User tertentu.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

#### Jawab: Authentication adalah proses verifikasi identitas pengguna sehingga sistem bisa mengetahui bahwa pengguna tersebut adalah siapa. Di sisi lain, authorization adalah proses menentukan pengguna mana yang telah lewati proses authentication bisa mengakses bagian mana di dalam sebuah sistem.

#### Proses yang dilakukan saat pengguna login adalah seperti berikut. Pengguna pertama kali masukkan username dan password mereka pada form login. Kemudian, Django akan periksa data yang dimasukkan pengguna terhadap entri data yang berada di basis data. Terakhir, pengguna yang sudah diverifikasi akan diberikan akses ke suatu halaman tertentu. Dalam kasus tugas ini, pengguna akan diberikan akses ke halaman main setelah login berhasil. Ini termasuk bagian dari authorization.

#### Django mengimplementasikan authentication dengan sistem dalam django.contrib.auth yang berisi fungsi seperti authenticate() dan login(). Dalam tugas ini, fungsi yang dipakai adalah login(). Dalam tugas ini, form yang dipakai dalam proses login adalah AuthenticationForm yang akan periksa input username dan password pengguna terhadap data dalam basis data. Kalau valid, pengguna akan diteruskan ke halaman utama setelah method login() mempertahankan sesi aktif pengguna sekarang. Di sisi lain, Django mengimplementasikan authorization dengan django.contrib.auth.decorators yang berisi decorators seperti @login_required (dalam tugas ini). Decorator @login_required akan periksa apakah pengguna sudah login atau belum. Kalau belum login, pengguna tidak diizinkan akses halaman main. Kalau sudah login, pengguna diizinkan akses ke halaman main.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

#### Jawab: Django mengingat pengguna yang telah login dengan membuat sebuah session ID. Setelah user lolos tahap verifikasi/authentication dari Django, Django langsung membuat session ID dan simpan ID tersebut di basis data. Selain itu, setiap kali user melakukan request, browser mengirimkan sebuah session cookie kepada server. Dengan informasi cookie ini, Django mampu mengambil session ID yang sesuai untuk user tersebut.

#### Selain session management, cookies juga digunakan untuk personalisasi, keranjang belanja, dan tracking. Semua hal ini dapat dilakukan karena cookies menyimpan informasi terkait user sehingga situs web mampu mengingat pengaturan dan preferensi user. Walaupun cookies berguna, cookies dapat bersifat bahaya. Pertama, cookies yang dikirim melalui website http saja dapat diambil hacker dengan cara sniffing. Apabila hacker memiliki cookie ini, mereka dapat menggunakan cookie tersebut untuk menipu situs web bahwa mereka adalah user yang terverifikasi. Kedua, cookies menyimpan informasi user yang dapat dibocorkan. Apabila cookies tidak disimpan dengan baik, seorang hacker mampu pakai cookie tersebut untuk mengetahui informasi terkait user dan menjualnya apabila mengandung data sensitif. Ketiga, cookies yang dipakai untuk tracking mampu membuat iklan menjadi lebih personalisasi ke user tertentu. Hal ini tentu saja mengurangi privasi user selama melakukan proses pencarian di internet karena setiap gerakan mereka mampu dilacak.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Jawab:

#### Checklist 1 (Fungsi Registrasi, Login, dan Logout):

#### a. Registrasi: Pertama, saya import UserCreationForm dan messages di views.py direktori aplikasi main. Kemudian, saya membuat fungsi register dalam views.py. Fungsi ini akan menerima input dari user dan melakukan tiga hal berikut:

#### i. Simpan input user.

#### ii. Tampilkan pesan berhasil

#### iii. Return user ke halaman main.

#### Selain itu, fungsi ini akan return sebuah halaman register.html yang menjadi sebuah halaman untuk user masukkan data supaya bisa login. Kemudian, saya membuat berkas register.html untuk menampilkan form ke user dalam bentuk tabel. Terakhir, saya import register ke urls.py dan membuat suatu path ke form register.

#### b. Login: Pertama, saya import AuthenticationForm, login, dan authenticate di views.py untuk melakukan autentikasi login user. Kemudian, saya membuat fungsi login_user dalam views.py. Fungsi ini akan membuat form autentikasi untuk terima input user. Selain itu, fungsi ini akan melakukan autentikasi user sebelum return ke main page. Fungsi ini juga membersihkan form untuk input user baru dan return sebuah halaman login untuk user. Kemudian, saya membuat berkas login.html untuk mmenampilkan form login ke user dalam bentuk tabel. Terakhir, saya import login_user ke urls.py dan membuat suatu path ke form login.

#### c. Logout: Pertama, saya import logout di views.py. Kemudian, saya membuat fungsi logout_user yang akan menghapus sesi user dan mengembalikkan user ke halaman main. Kemudian, saya membuat sebuah tombol logout di berkas main.html yang akan pergi ke bagian logout di path urls dan panggil fungsi logout_user. Terakhir, saya import logout_user ke urlls.py dan membuat suatu path untuk logout.

#### Checklist 2 (2 akun 3 item): Pertama, saya jalankan `python manage.py runserver` dan pergi ke pranala lokal host, yaitu `http://localhost:8000/login/`. Kemudian, saya membuat dua akun baru dan masing-masing akun berisi tiga produk berbeda. Berikut adalah pranala drive menuju gambar konten kedua akun di lokal: https://drive.google.com/drive/folders/15YbtzMX7CLws6X3deIZ_Zva5nUmHaT2V?usp=drive_link

#### Checklist 3 (Menghubungkan Product dengan User): Pertama, saya membuat sebuah user supaya produk awal bisa dihubungkan ke user pertama. Kemudian, saya import User ke models.py supaya bisa digunakan. Kemudian, saya tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` di model ProductEntry supaya produk bisa dihubungkan ke user melalui sebuah relationship. Kemudian, saya modifikasi bagian blok if di create_product_entry menjadi berikut:

```python
if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
```

#### Kurang lebih, bagian ini akan menyimpan product_entry dulu tanpa simpan ke basis data. Setelah itu, kode ini akan menghubungkan produk ke objek User dari hasil request.user yang berupa user yang login. Setelah itu, kode ini akan simpan data tersebut ke basis data. Kemudian, saya saring/filter object produk sesuai objek user sekarang yang sedang login. Kemudian, saya ubah name menjadi username dari user yang sedang login ke halaman main. Kemudian saya jalankan `python manage.py makemigrations`. Kemudian, saya pilih opsi 1 untuk menetapkan default value untuk field user pada semua row yang sudah dibuat. Kemudian, saya tetapkan user dengan ID 1 pada model yang sudah ada. Kemudian, saya jalankan `python manage.py migrate`. Terakhir, saya import os di settings.py direktori proyek (closure_shop) dan ubah bagian DEBUG menjadi not PRODUCTION sehingga pws tidak rungkad dan bebannya lebih ringan di pws.

#### Checklist 4 (Cookies, Login, Logout): Pertama, saya import datetime, HttpResponseRedirect, dan reverse. Kemudian, saya update fungsi login_user di blok `if form.is_valid()`. Blok ini akan melakukan login terlebih dahulu. Setelah itu, blok ini akan buat response berupa balik ke halaman main dan buat cookie last login yang ditambahkan ke dalam response. Kemudian, saya tambahkan `'last_login': request.COOKIES['last_login'],` di bagian context di views.py. Kode ini akan menambahkan informasi berupa waktu terakhir user login. Kemudian, saya update fungsi logout_user sehingga cookies last login bisa dihapus pas user logout dan kembali ke halaman utama. Terakhir, saya tambahkan tag html di paling bawah yang berisi informasi terakhir kali user login.

#### Checklist 5 (Jawab pertanyaan): Saya hanya menambahkan bagian untuk jawaban tugas 4 dan tulis jawaban di bagian tersebut.

#### Checklist 6 (git add, commit, push): Pertama, saya menjalankan perintah `git add .` untuk menambahkan semua file yang berubah pada staging. Kedua, saya menjalankan perintah `git commit -m "[Pesan]"` untuk merekam perubahan yang sudah masuk staging di history repositori. Terakhir, saya menjalankan perintah `git push origin main` untuk mendorong perubahan ke branch main repositori closure-shop di GitHub saya.

### ===============TUGAS 5===============

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

#### Jawab: CSS selector memiliki empat urutan prioritas. Prioritas pertama adalah inline styles seperti `<h1 style="color: green;">` yang memiliki nilai spesifisitas 1000. Prioritas kedua adalah IDs seperti #home yang memiliki nilai spesifisitas 100. Prioritas ketiga adalah class, pseudo class, dan attribute selectors seperti .sample, :click, dan [href] yang memiliki nilai spesifisitas 10. Prioritas keempat adalah elements dan pseudo elements seperti h2 dan ::after yang memiliki nilai spesifisitas 1. Selain itu, CSS ada satu tag, yaitu !important yang mampu override semua selector, bahkan inline styles akan dioverride.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

#### Jawab: Disklaimer: Jawaban saya pada soal ini hanya sebuah contoh dan saya tidak bermaksud untuk mempromosikan atau merendahkan aplikasi tersebut. Responsive design menjadi konsep penting dalam pengembangan aplikasi web karena desain ini meningkatkan penampilan aplikasi web. Apabila kita membuat aplikasi web tanpa responsive design, aplikasi web kita bisa saja terlihat berbeda atau terlihat buruk di perangkat layar kecil seperti handphone dan tablet. Dengan responsive design, kita mampu mengatur tampilan aplikasi web kita pada perangkat yang berbeda sehingga tampilannya baik dan elegan. Beberapa contoh aplikasi yang sudah menerapkan responsive design adalah [Tokopedia](https://www.tokopedia.com/), [Shopee](https://shopee.co.id/), dan [Arknights](https://www.arknights.global/). Apabila kita buka aplikasi web ini pada perangkat berbeda seperti laptop dan hp, tampilannya terlihat berbeda dan indah di kedua perangkat tersebut. Beberapa contoh aplikasi yang belum menerapkan responsive design adalah [SIAKNG](https://academic.ui.ac.id/main/Authentication/), [Webmail UI](https://webmail.ui.ac.id/roundcube2/?_task=logout), dan [siasisten](https://siasisten.cs.ui.ac.id/login/). Apabila kita buka aplikasi web ini pada perangkat berbeda seperti laptop dan hp, tampilannya terlihat berbeda dan tampilannya di hp terlihat kecil sehingga perlu di zoom supaya bisa lihat lebih baik. Saya ingin menyampaikan sekali lagi, contoh dalam jawaban ini hanya merupakan contoh dan berdasarkan fakta dan tidak bermaksud untuk mempromosikan atau merendahkan aplikasi tersebut.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

#### Jawab: Margin adalah ruang terluar dari suatu elemen. Margin digunakan untuk memisahkan sebuah elemen dengan elemen lain. Margin bisa diimplementasikan secara menyeluruh (seperti `margin: 20px;`) atau satu per satu (seperti `margin-top: 10px;`).

#### Border adalah sebuah garis antara margin dan padding yang bisa diubah dengan styling tertentu, seperti dotted, solid, dashed, dll. Border bisa diimplementasikan dengan dua cara seperti margin. Cara pertama adalah secara menyeluruh, seperti `border: 5px dotted purple;`. Cara kedua adalah secara satu per satu, seperti `border-right: 5px solid green;`.

#### Padding adalah ruang antara border dan konten. Padding digunakan untuk membuat sebuah ruang di dalam border tertentu supaya konten terlihat lebih rapi. Padding bisa diimplementasikan dengan dua cara seperti margin dan border. Cara pertama adalah secara menyeluruh, seperti `padding: 17px;`. Cara kedua adalah secara satu per satu, seperti `pading-bottom: 15px;`.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

#### Jawab: Flexbox adalah sebuah desain satu dimensi seperti baris atau kolom. Flexbox bisa mengatur posisi, arah, ruang antara komponen dalam sebuah kontainer. Flexbox digunakan untuk membuat navigation bar, kartu, menaruh elemen di tengah, dll. Di sisi lain, grid layout adalah desain dua dimensi seperti suatu tabel yang memiliki baris dan kolom. Grid layout adalah suatu desain yang lebih kompleks daripada flexbox. Grid layout digunakan untuk layout kompleks, galeri gambar, antarmuka dashboard, dll.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

#### Jawab:

#### Checklist 1 (Edit dan Delete):

#### Fungsi edit: Pertama, saya buat fungsi edit_product di views.py. Fungsi ini akan menerima request dan object id, cari product yang mau diubah, tampilkan form kepada user, simpan hasil perubahan, dan tampilkan halaman main kepada user. Kemudian, saya buat berekas edit_product.html di direktori templates yang menjadi tampilan utama form edit product. Kemudian, saya import edit_product di urls.py. Kemudian, saya membuat path url di dalam urlpatterns supaya fungsi edit_product bisa diakses. Terakhir, saya tambahkan kode berikut sejajar dengan elemen td lainnya di main.html:

```
    <td>
        <a href="{% url 'main:edit_product' product_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
```

#### Tujuan kode di atas adalah menambahkan primary key product_entry sebagai parameter yang akan diteruskan ke method edit_product di views.py.

#### Fungsi delete: Pertama, saya buat fungsi delete_product di views.py. Fungsi ini akan menerima request dan object id, cari product yang mau dihapus, dan hapuskan product tersebut. Kemudian, saya import delete_product di urls.py. Kemudian, saya membuat path url di urlpatterns menuju fungsi yang sudah diimpor. Terakhir, saya tambahkan kode berikut sejajar dengan elemen td lainnya di main.html:

```
    <td>
        <a href="{% url 'main:delete_product' product_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
```

#### Tujuan kode di atas adalah menambahkan primary key product_entry sebagai parameter yang akan diteruskan ke method delete_product di views.py.

#### Checklist 2 (Kustomisasi desain): Pertama, saya tambahkan meta tag viewport agar halaman web dapat menyesuaikan ukuran dan perilaku perangkat mobile. Kemudian, saya menyambungkan template Django dengan Tailwind. Kemudian, saya import font Monospace dari Google Fonts dan set semua teks di body menjadi Monospace di global.css. Kemudian, saya ubah warna border menjadi warna jingga di global.css. Kemudian saya melakukan hal berikut untuk masing-masing subschecklist pada checklist 2:

#### a. Kustomisasi halaman login, register, tambah product, dan edit product:

#### i. Halaman login: Pertama, saya salin dari tutorial 4. Kemudian, saya tanya teman saya tentang cara mengganti warna dan animasi. Dalam login.html, saya ganti warna buttton sign in dari indigo dengan hexcode dua warna berbeda dan hover delay 300ms sehingga animasinya lebih elegan. Terakhir, saya ganti warna teks register supaya lebih mudah dilihat dan menarik.

#### ii. Register: Pertama, saya salin dari tutorial 4. Kemudian, saya coba melihat elemen yang mau saya ubah. Kemudian, saya ubah button Register sehingga efek dan warnanya mirip dengan button sign in di login.html. Kemudian, saya ubah warna teks Login Here seperti warna teks register dan atur hover delay 300ms. Terakhir, saya ubah warna border form menjadi warna yang sama dengan button sebelum dihover.

#### iii.Tambah product: Pertama, saya salin dari tutorial 4. Kemudian, saya mengubah warna background. Terakhir, saya mengubah warna form dan button di bagian bawah sehingga mirip dengan button register dan sign in.

#### iv. Edit product: Pertama, saya salin dari tutorial 4. Kemudian, saya mengubah warnanya seperti warna di halaman tambah product. Terakhir, saya mengubah warna button di bagian bawah sehingga mirip dengan button register, sign in, dan add new product entry.

#### b. Kustomisasi daftar product: Pertama, saya salin dari tutorial 4. Kemudian, saya taruh gambar bernama empty.png yang merupakan gambar yang ditampil saat toko kosong di atas pesan toko kosong. Kemudian, saya hapuskan efek-efek yang ada pada card tutorial 4. Terakhir, saya ubah warna card.

#### c. Button Edit dan Delete: Pertama, saya salin dari tutorial 4. Kemudian, saya mengubah tombol edit dan delete menjadi teks. Kemudian, saya mengubah bentuk tombol edit dan delete supaya berbeda. Terakhir, saya tambahkan popup konfirmasi apakah mau delete item tersebut atau tidak.

#### d. Navigation Bar (Navbar): Pertama, saya salin template navbar dari tutorial 4.

#### Checklist 3 (Jawab pertanyaan): Saya hanya menambahkan bagian untuk jawaban tugas 5 dan tulis jawaban di bagian tersebut.

#### Checklist 4 (git add, commit, push): Pertama, saya menjalankan perintah `git add .` untuk menambahkan semua file yang berubah pada staging. Kedua, saya menjalankan perintah `git commit -m "[Pesan]"` untuk merekam perubahan yang sudah masuk staging di history repositori. Terakhir, saya menjalankan perintah `git push origin main` untuk mendorong perubahan ke branch main repositori closure-shop di GitHub saya.

##### Referensi: chatGPT, tutorial 0, 1, 2, 3, dan 4 PBP, [Quora-Why is JSON so popular](https://www.quora.com/Why-is-JSON-so-popular), [Dokumentasi Django-Forms](https://docs.djangoproject.com/en/5.1/topics/forms/), [Dokumentasi Django-CSRF](https://docs.djangoproject.com/en/5.1/ref/csrf/), [W3 Schools-CSS Specificity](https://www.w3schools.com/css/css_specificity.asp), [Why is Responsive Design So Important?](https://www.webfx.com/web-design/learn/why-responsive-design-important/)

##### Collaborator: Thorbert Anson Shi
