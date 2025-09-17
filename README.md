# -----Tugas 2------ #
1.  
    Langkah awal saya dalam mengerjakan Tugas 2 PBP ini adalah menentukan nama project, dan akhirnya saya memilih League Locker. Setelah itu, saya membuat repositori baru di GitHub lalu melakukan clone ke folder lokal. Dari folder hasil clone tersebut, saya membuka command prompt untuk membuat direktori sekaligus mengaktifkan virtual environment. Perintah yang saya gunakan adalah python -m venv env untuk membuat env, lalu env\Scripts\activate untuk mengaktifkannya.

    Pada tahap konfigurasi environment, inisiasi schema saya ubah menjadi "tugas_individu". Setelah itu selesai, saya langsung melanjutkan dengan menjalankan server menggunakan perintah python manage.py migrate dan python manage.py runserver.

    Begitu server berhasil dijalankan, saya mengunggah project versi “setengah jadi” ini ke GitHub. Langkah pertama adalah menghubungkan repositori lokal dengan repositori GitHub yang sudah dibuat sebelumnya. Setelah itu, saya membuat branch baru dengan nama master. Lalu, saya melakukan git add, git commit, dan git push agar project tersebut berhasil terunggah ke GitHub. Selain itu, saya juga menambahkan file .gitignore supaya file-file yang tidak diperlukan tidak ikut terunggah.

    Pada langkah berikutnya, saya mulai masuk ke konfigurasi Django dan mengimplementasikan Model-View-Template (MVT) sebelum menambahkan project ke Pacil Web Service (PWS). Pertama-tama, saya memastikan virtual environment di folder league-locker sudah aktif. Setelah itu, saya membuat aplikasi baru bernama main dengan menjalankan perintah python manage.py startapp main.

    Setelah aplikasi main berhasil dibuat, saya membuat template sederhana berupa file HTML untuk menampilkan informasi awal project League Locker saya. Isinya hanya nama project, nama saya, dan kelas, supaya saya bisa memastikan struktur MVT sudah berjalan dengan baik.

    Berikutnya, saya mengubah file models.py di aplikasi main sesuai ketentuan soal. Model yang saya buat berisi atribut name, price, description, thumbnail, category, dan is_featured. Setelah model selesai, saya menjalankan migrasi agar database menyesuaikan dengan model tersebut.

    Langkah setelah itu adalah melakukan modifikasi template agar data lebih sesuai, serta menambahkan routing di urls.py supaya halaman bisa diakses dengan benar lewat browser.

    Setelah semua bagian dasar MVT selesai, saya baru lanjut menambahkan project ke Pacil Web Service (PWS). Di tahap ini, saya membuat project baru dan menyimpan project credentials yang diperlukan. Lalu, saya menambahkan konfigurasi environs dan menyesuaikannya dengan environment di file .env.prod.

    Selanjutnya, saya memperbarui file settings.py dengan menambahkan URL deployment ke bagian ALLOWED_HOSTS agar project bisa diakses melalui server PWS. Terakhir, saya melakukan git push ke PWS untuk deployment, sekaligus git push ke GitHub supaya semua perubahan terbaru juga tersimpan di repositori.

2. Berikut merupakan bagan request client ke web apliksi berbasis Django.
![alt text](image.png)

3. settings.py seperti "pusat pengaturan" yang ada di project Django. File ini menampung konfigurasi penting, speerti database, daftar aplikasi yang aktif, middleware. Jadi kalau kita mau ganti/nambah/atur kayak allowed hosts gitu bisa di file ini.

4. Cara kerja migrasi database itu ada dua. Pertama dengan command "python manage.py makemigrations", disini Django akan mencatat perubahan model yang telah kita buat. Kedua dengan command "python manage.py migrate", pada command ini Django akan menjalankan perubahan tersebut ke database. Jadi migrasi ini fungsinya untuk sinkronisasi antara database dan model yang sudah kita buat di kode.

5. Karena pada Django sudah terdapat fitur-fitur penting kayak login user, admin panel, database, hingga routing. Jadi pemula kayak kita gaperlu pusing-pusing cari komponen tambahan lagi. Selain itu, Django juga mudah dipahami alurnya dan memiliki dokumentasi yang besar, ini dapat membantu para pemula belajar ngoding dengan rapi dan teratur.

6. Terima kasih banyak untuk tim Asdos terutama kak Clarence dan kak Isa yang membantu saya saat tidak dapat membuat aplikasi main pada tutorial 1. 





# -----Tugas 3------ #
1. Data delivery diperlukan agar server dan client dapat saling bertukar informasi, sehingga platform dapat berjalan dengan lancar dan dapat menampilkan data ke pengguna.

2. Mengapa json lebih banyak dipakai sekarang dibanding xml? karena xml ini secara usia lebih tua, lalu memiliki struktur yang tidak mudah, memiliki banyak tag, dan ukurannya yang lebih besar jika dibandingkan dengan json yang lebih simpel, lebih ringan, mudah dibaca manusia dan mesin. Jadi, json lebih populer karena dia lebih praktis dan parsingnya lebih cepat daripada xml.

3. Method is_valid() dipakai untuk mengecek apakah data yang diisi oleh user di form sudah sesuai aturan atau belum. Misal, field harga harus diisi oleh angka atau field tumbnail harus diisi dengan url gambarnya. Kalau is_valid() hasilnya True, berarti data aman untuk disimpan ke database. Kalau tidak, akan muncul error.

4. csrf_token dipakai untuk keamanan form. Dia bakal mencegah serangan yang namanya CSRF (Cross-Site Request Forgery), yaitu kondisi ketika penyerang bikin user tanpa sadar mengirim request berbahaya ke server (misal transfer uang atau ubah password). Kalau tidak pakai csrf_token, penyerang bisa bikin form palsu di website lain, lalu memaksa user login kita untuk submit data ke server kita. Akibatnya, sistem bisa dipakai tanpa izin user yang asli.

5. Langkah awal yang saya lakukan adalah dengan memastikan struktur direktori saya sudah sesuai dengan yang terdapat di tutorial 2. Lalu, saya mengimplementasikan skeleton sebagai kerangka view yang berfungsi untuk memastikan adanya konsistensi dalam desain situs web kita serta memperkecil kemungkinan terjadinya redundansi kode. Lalu, saya lanjut membuat form input data dan menampilkan data dari project saya (league locker) pada HTML dengan membuat struktur forms, membuat beberapa fungsi baru di views.py, lalu routing url di urls.py, serta menambahkan file HTML dengan menyesuaikan beberapa variabel berdasarkan field saya yang terdapat pada models.

Selanjutnya saya melalukan pengembalian data dalam bentuk xml dan json dengan menambahkan beberapa function seperti show_xml dan show_json, tidak lupa juga untuk menambahkan path url di dalam file urls.py. Selain itu, saya juga melakukan pengembalian data berdasarkan ID dalam bentuk xml dan json. Anyway, di dalam field models project saya ini belum terdapat id dari itemnya, jadi saya menambahkan field baru dengan menggunakan uuid dan langsung melakukan migrate. Setelah ID item ada, pada tahap ini saya menambahkan beberapa function yaitu show_xml_by_id dan show_json_by_id, tidak lupa juga untuk menambahkan path url di dalam file urls.py. 

Setelah itu saya mencoba runserver untuk melihat project saya di local host, lalu saya menambahkan item baru di project saya. Dengan kita menambahkan item baru, kita dapat melihat ID dari item tersebut dan melihat data tersebut di Postman. Setelah semua step diatas selesai, selanjutnya saya melakukan push di github dan pws, serta menambahkan item pada project pws saya.


6. Terima kasih banyak kakak Asdos telah membantu men-debug kekeliruan saya saat menambahkan news di project PWS. 

7. Berikut merupakan screenshot hasil akses URL pada postman
xml:
![alt text](<Screenshot 2025-09-17 003210.png>)
json:
![alt text](<Screenshot 2025-09-17 003342.png>)