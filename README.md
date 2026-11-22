# TP5 Chatbot RAG SOP Akademik

## Deskripsi

Proyek ini merupakan tahap awal pengembangan Chatbot RAG SOP Akademik untuk praktikum Cloud AI. Dataset yang digunakan bersifat simulasi dan terdiri dari lima dokumen SOP dalam format TXT.

## Struktur Proyek

```text
TP5-Chatbot-RAG-Akademik/
├── data/
│   ├── raw/
│   │   ├── sim-001.txt
│   │   ├── sim-002.txt
│   │   ├── sim-003.txt
│   │   ├── sim-004.txt
│   │   └── sim-005.txt
│   └── storage/
│       ├── sim-001.txt
│       └── sim-002.txt
├── manifest.json
├── scripts/
│   └── validate.py
├── reports/
│   └── validation.json
├── diagrams/
│   └── architecture.md
├── use-case.md
└── README.md
```

## Dataset

Dataset terdiri dari lima dokumen simulasi:

1. SIM-001 - Prosedur Pengajuan Surat Akademik
2. SIM-002 - Prosedur Peminjaman Ruang Kampus
3. SIM-003 - Prosedur Konsultasi Akademik Mahasiswa
4. SIM-004 - Prosedur Penggunaan Laboratorium Komputer
5. SIM-005 - Prosedur Layanan Perpustakaan Kampus

Seluruh dokumen merupakan data simulasi untuk keperluan praktikum.

## Validasi

Validasi dataset dilakukan menggunakan Python melalui file `scripts/validate.py`.

Validasi mencakup:
- kelengkapan metadata;
- pengecekan document ID duplikat;
- pengecekan keberadaan file;
- pengecekan konten dokumen;
- pengecekan encoding UTF-8;
- perhitungan SHA-256.

Hasil validasi akhir menunjukkan:

```text
Total dokumen  : 5
Dokumen valid  : 5
Dokumen invalid: 0
Status         : SUCCESS
```

## Negative Test

Negative test dilakukan dengan membuat salah satu dokumen tidak memenuhi persyaratan konten. Hasil pengujian menunjukkan:

```text
Total dokumen  : 5
Dokumen valid  : 4
Dokumen invalid: 1
Status         : FAILED
```

Setelah dokumen diperbaiki, validasi kembali menghasilkan:

```text
Total dokumen  : 5
Dokumen valid  : 5
Dokumen invalid: 0
Status         : SUCCESS
```

## Storage dan Integritas

Dua dokumen, yaitu `sim-001.txt` dan `sim-002.txt`, disalin dari folder `data/raw/` ke `data/storage/`.

SHA-256 file sebelum dan sesudah penyimpanan dibandingkan. Hasil perbandingan menunjukkan hash kedua file tetap sama sehingga integritas file terjaga.

## Arsitektur RAG

Arsitektur pengembangan RAG dijelaskan pada:

`diagrams/architecture.md`

Alur utama:

```text
Dataset
   ↓
Validasi
   ↓
Storage
   ↓
Parsing / Cleaning
   ↓
Chunking + Metadata
   ↓
Embedding
   ↓
Vector Index
   ↓
Retrieval Top-K
   ↓
Grounded Prompt
   ↓
LLM
   ↓
Jawaban + Rujukan
```

Tahap embedding, vector index, retrieval, dan LLM merupakan bagian pengembangan RAG pada tahap berikutnya.