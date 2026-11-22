# Arsitektur Chatbot RAG SOP Akademik

```text
┌──────────────────────────────┐
│        DATA SIMULASI         │
│       5 Dokumen TXT         │
│          data/raw/           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       VALIDASI DATASET       │
│        scripts/validate.py   │
│  - Metadata                  │
│  - File existence            │
│  - Encoding UTF-8            │
│  - SHA-256                   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       LOCAL STORAGE          │
│        data/storage/         │
│      Copy + Read-back        │
│       + Checksum             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       RAG PIPELINE           │
│ Parsing → Cleaning → Chunking│
│ → Embedding → Vector Index   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          RETRIEVAL           │
│       Top-K Dokumen          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      GROUNDED PROMPT         │
│  Pertanyaan + Context       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│           LLM                │
│      Jawaban + Rujukan       │
└──────────────────────────────┘


Batas Akses:
- data/raw      → sumber dataset
- data/storage  → penyimpanan lokal
- manifest.json → metadata dataset
- reports/      → hasil validasi
- API/LLM       → tahap pengembangan berikutnya