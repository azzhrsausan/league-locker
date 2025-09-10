
1.  

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


