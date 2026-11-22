# Use Case Chatbot RAG SOP Akademik

## Tujuan

Chatbot RAG SOP Akademik dibuat untuk membantu mahasiswa memperoleh informasi mengenai prosedur layanan akademik berdasarkan dokumen yang telah disiapkan dan divalidasi. Chatbot dapat menjawab pertanyaan seputar pengajuan surat akademik, peminjaman ruang kampus, konsultasi akademik, penggunaan laboratorium komputer, dan layanan perpustakaan.

## Kebutuhan Data

Chatbot membutuhkan dokumen SOP dalam bentuk TXT sebagai sumber informasi. Pada tahap TP5 digunakan lima dokumen simulasi yang bersifat sintetis. Setiap dokumen memiliki metadata berupa document ID, judul, sumber, versi, tingkat akses, dan lokasi file. Data juga dilengkapi SHA-256 untuk memastikan integritas dokumen. Dokumen tersebut akan menjadi sumber yang dapat ditelusuri pada tahap pengembangan RAG berikutnya.