# Reflection TP5 - Chatbot RAG SOP Akademik

## Refleksi

Pada pengerjaan TP5, kelompok kami membangun dataset simulasi untuk kebutuhan pengembangan Chatbot RAG SOP Akademik. Dataset terdiri dari lima dokumen TXT yang berisi prosedur layanan akademik. Setiap dokumen dilengkapi metadata melalui `manifest.json` dan kemudian divalidasi menggunakan script Python. Proses ini membantu kami memahami bahwa data yang akan digunakan oleh sistem AI harus diperiksa terlebih dahulu sebelum masuk ke tahap RAG.

Salah satu kegagalan yang terjadi adalah ketika kami melakukan negative test pada proses validasi. Salah satu dokumen dibuat memiliki konten yang kosong atau terlalu pendek sehingga hasil validasi menunjukkan empat dokumen valid dan satu dokumen invalid. Status validasi berubah menjadi `FAILED`. Dari pengujian tersebut kami mengetahui bahwa proses validasi tidak hanya digunakan untuk menghasilkan status berhasil, tetapi juga untuk menemukan masalah pada dataset. Setelah dokumen diperbaiki, proses validasi dijalankan kembali dan menghasilkan lima dokumen valid dengan status `SUCCESS`. Pengujian ini menunjukkan pentingnya melakukan validasi dan negative test sebelum data digunakan lebih lanjut.

Untuk penyimpanan, pada tahap ini kami menggunakan local storage karena lebih sederhana dan mudah dikontrol. File dapat disimpan langsung pada folder proyek dan proses read-back dapat dilakukan tanpa koneksi internet atau layanan cloud. Kelemahannya adalah data hanya berada pada lingkungan lokal sehingga belum memiliki fleksibilitas dan skalabilitas seperti cloud storage. Cloud dapat memberikan akses yang lebih mudah dari berbagai lingkungan serta mendukung pengembangan sistem yang membutuhkan penyimpanan lebih besar. Namun, penggunaan cloud juga perlu memperhatikan keamanan, akses, konfigurasi, dan kemungkinan biaya layanan. Untuk tahap TP5, local storage sudah cukup karena fokus utama adalah membuktikan proses penyimpanan dan integritas data melalui perbandingan SHA-256.

Pada TP8, dataset yang sudah divalidasi akan menjadi dasar untuk pengembangan pipeline RAG. Rencana pengembangannya adalah melakukan parsing dan cleaning dokumen, membagi dokumen menjadi beberapa chunk, mempertahankan metadata, membuat embedding, kemudian menyimpan embedding pada vector index. Setelah itu sistem dapat melakukan retrieval berdasarkan pertanyaan pengguna dan mengambil beberapa dokumen yang paling relevan. Context hasil retrieval kemudian digunakan untuk membuat grounded prompt sehingga jawaban chatbot tetap berdasarkan sumber dokumen. Dengan proses tersebut, hasil dari TP5 dapat digunakan sebagai fondasi untuk membangun Chatbot RAG pada tahap berikutnya.

# Reflection TP6 — AI Method Selection & Reproducible Mini Experiment

## 1. Hal yang Dipelajari

Pada TP6, saya mempelajari cara memilih metode AI yang sesuai dengan masalah yang ingin diselesaikan. Pada proyek Chatbot RAG Akademik, masalah yang digunakan adalah menemukan dokumen yang paling relevan berdasarkan pertanyaan pengguna.

Metode yang dipilih adalah embedding dan semantic search menggunakan model `embeddinggemma` melalui Ollama Local. Metode ini dibandingkan dengan keyword search sebagai baseline.

## 2. Hasil Eksperimen

Eksperimen menggunakan 5 dokumen data sintetis dan 5 test case. Semantic search mampu melakukan pencarian berdasarkan kemiripan makna antara pertanyaan dengan isi dokumen.

Dari hasil pengujian, rata-rata waktu semantic search sekitar 2,09 detik per query. Sementara keyword search memiliki waktu yang jauh lebih cepat, sekitar 0,0002–0,0003 detik per query.

Hasil tersebut menunjukkan bahwa semantic search membutuhkan waktu lebih lama karena proses pembuatan embedding, tetapi memiliki pendekatan pencarian berdasarkan makna yang lebih sesuai untuk pengembangan chatbot RAG.

## 3. Kendala yang Ditemukan

Kendala utama adalah waktu proses semantic search yang lebih lambat dibandingkan keyword search. Selain itu, hasil retrieval belum selalu sempurna karena dokumen yang memiliki makna mirip dapat memiliki skor similarity yang berdekatan.

Eksperimen juga menunjukkan bahwa kualitas hasil sangat bergantung pada kualitas dokumen dan test case yang digunakan.

## 4. Risiko dan Perbaikan

Beberapa risiko yang perlu diperhatikan adalah kesalahan retrieval, hallucination pada tahap generasi jawaban, latency, serta kemungkinan penggunaan data yang tidak sesuai.

Untuk pengembangan berikutnya, sistem perlu menggunakan dataset yang lebih banyak dan test case yang lebih beragam. Hasil retrieval juga perlu dievaluasi secara lebih terstruktur agar dapat mengetahui tingkat keberhasilan sistem.

## 5. Hubungan dengan TP5 dan Tahap Berikutnya

TP6 menggunakan dataset dan struktur penyimpanan yang telah dibuat pada TP5. Eksperimen ini menjadi dasar untuk pengembangan sistem RAG berikutnya.

Hasil TP6 dapat digunakan sebagai dasar untuk evaluasi pada TP10, integrasi sistem pada TP12, dan pengembangan produk pada TP16.

## 6. Kesimpulan

Melalui TP6, saya memahami bahwa pemilihan metode AI harus disesuaikan dengan kebutuhan sistem dan tidak hanya berdasarkan metode yang terlihat paling canggih.

Semantic search dipilih karena sesuai dengan kebutuhan pencarian dokumen berdasarkan makna. Keyword search digunakan sebagai baseline untuk mengetahui perbedaan kecepatan dan pendekatan retrieval.

Eksperimen yang dibuat juga dapat dijalankan kembali secara lokal sehingga hasilnya lebih mudah direproduksi dan dikembangkan pada tahap berikutnya.