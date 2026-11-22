{
  "experiment": "TP6 Semantic Search",
  "model": "embeddinggemma",
  "document_count": 2,
  "test_count": 5,
  "results": [
    {
      "id": "TC-001",
      "query": "Apa tujuan dari panduan akademik?",
      "expected": "Dokumen yang menjelaskan panduan akademik",
      "top_result": {
        "filename": "sim-001.txt",
        "score": 0.3484446790353151
      },
      "latency_seconds": 2.1122,
      "all_results": [
        {
          "filename": "sim-001.txt",
          "score": 0.3484446790353151
        },
        {
          "filename": "sim-002.txt",
          "score": 0.23124207651119616
        }
      ]
    },
    {
      "id": "TC-002",
      "query": "Bagaimana mahasiswa mendapatkan informasi akademik?",
      "expected": "Dokumen yang berkaitan dengan informasi akademik",
      "top_result": {
        "filename": "sim-001.txt",
        "score": 0.4175153835196638
      },
      "latency_seconds": 2.0945,
      "all_results": [
        {
          "filename": "sim-001.txt",
          "score": 0.4175153835196638
        },
        {
          "filename": "sim-002.txt",
          "score": 0.32921752954569156
        }
      ]
    },
    {
      "id": "TC-003",
      "query": "Apa aturan yang harus diperhatikan mahasiswa?",
      "expected": "Dokumen yang menjelaskan aturan mahasiswa",
      "top_result": {
        "filename": "sim-002.txt",
        "score": 0.38748607598898716
      },
      "latency_seconds": 2.1029,
      "all_results": [
        {
          "filename": "sim-002.txt",
          "score": 0.38748607598898716
        },
        {
          "filename": "sim-001.txt",
          "score": 0.33682677838018643
        }
      ]
    },
    {
      "id": "TC-004",
      "query": "Bagaimana cara mahasiswa mengikuti proses perkuliahan?",
      "expected": "Dokumen yang berkaitan dengan proses perkuliahan",
      "top_result": {
        "filename": "sim-001.txt",
        "score": 0.35916033835633104
      },
      "latency_seconds": 2.0992,
      "all_results": [
        {
          "filename": "sim-001.txt",
          "score": 0.35916033835633104
        },
        {
          "filename": "sim-002.txt",
          "score": 0.3376244346212186
        }
      ]
    },
    {
      "id": "TC-005",
      "query": "Di mana mahasiswa dapat menemukan informasi yang dibutuhkan?",
      "expected": "Dokumen yang paling relevan dengan pertanyaan",
      "top_result": {
        "filename": "sim-002.txt",
        "score": 0.3823623839500656
      },
      "latency_seconds": 2.115,
      "all_results": [
        {
          "filename": "sim-002.txt",
          "score": 0.3823623839500656
        },
        {
          "filename": "sim-001.txt",
          "score": 0.3667442100990223
        }
      ]
    }
  ]
}